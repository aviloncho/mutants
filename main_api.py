from typing import List
from fastapi import FastAPI, Depends, Response, status
from sqlalchemy.orm import Session

import mutant
import api.schemas as schemas
import db.crud as crud
import db.models as models
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    """Welcome message."""
    return {"message": "Welcome to DNA Analysis"}


@app.post("/mutant/")
async def analyze_dna(dna: schemas.HumanDNA,
                      response: Response,
                      db: Session = Depends(get_db)):
    """
    Check if DNA is from a mutant human.
    Responses:
        200 is mutant.
        403 is not mutant.
    """
    dna_analysis = crud.get_dna_analysis(db, human_dna=dna)

    if dna_analysis:
        is_mutant = dna_analysis.is_mutant
    else:
        is_mutant = mutant.is_mutant(dna.dna)
        dna_analysis = crud.create_dna_analysis(
            db,
            human_dna=dna,
            mutant=is_mutant
        )

    if is_mutant:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_403_FORBIDDEN

    dna_response = schemas.HumanDNAResponse(
        dna=dna.dna,
        dna_hash=dna_analysis.dna_hash
    )

    return dna_response


@app.get("/stats/", response_model=schemas.DnaStats)
def get_mutant_stats(db: Session = Depends(get_db)):
    stats = crud.get_stats(db)
    return stats


@app.get("/dnas/", response_model=List[schemas.DnaAnalysis])
def read_dnas_analysis(skip: int = 0,
                       limit: int = 100,
                       db: Session = Depends(get_db)):
    dna_analysis = crud.get_dnas_analysis(db, skip=skip, limit=limit)
    return dna_analysis


@app.get("/dnas/{dna_hash}", response_model=schemas.DnaAnalysis)
def read_dna_analysis(dna_hash: str,
                      db: Session = Depends(get_db)):
    dna_analysis = crud.get_dna_analysis_by_hash(db, dna_hash)
    return dna_analysis
