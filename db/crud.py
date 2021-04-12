from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

import db.models as models
import api.schemas as schemas
from utils import hash_utils


def get_dnas_analysis(db: Session, skip: int = 0, limit: int = 100):
    """Get all DnaAnalysis stored in the database."""
    return db.query(models.DnaAnalysis).offset(skip).limit(limit).all()


def get_dna_analysis(db: Session,
                     human_dna: schemas.HumanDNA,):
    """Get specific DnaAnalysis stored in the database."""
    str_dna, hash_dna = hash_utils.hash_md5(human_dna)

    try:
        dna_analysis = db.query(models.DnaAnalysis).filter_by(
            dna_hash=hash_dna.hexdigest()
        ).first()
    except NoResultFound:
        dna_analysis = None

    return dna_analysis


def create_dna_analysis(db: Session,
                        human_dna: schemas.HumanDNA,
                        mutant: bool = False):
    """
    Create a new DnaAnalysis record on the database.
    """
    str_dna, hash_dna = hash_utils.hash_md5(human_dna)

    db_dna = models.DnaAnalysis(
        dna_hash=hash_dna.hexdigest(),
        dna=str_dna,
        is_mutant=mutant
    )

    db.add(db_dna)
    db.commit()
    db.refresh(db_dna)
    return db_dna


def get_stats(db: Session):
    """
    Get DumanDNA stats from database.
    Mutant DNA's / Total Human DNA's
    """
    total = db.query(models.DnaAnalysis).count()
    mutant = db.query(models.DnaAnalysis).filter(
        models.DnaAnalysis.is_mutant
    ).count()

    ratio = 0
    if mutant > 0 and total > 0:
        ratio = mutant / total

    stats = schemas.DnaStats(
        count_human_dna=total,
        count_mutant_dna=mutant,
        ratio=float(str(ratio)[:3])
    )

    return stats
