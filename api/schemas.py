from datetime import datetime
from pydantic import BaseModel
from typing import List


class HumanDNA(BaseModel):
    """
    HumanDNA model. Specify DNA object for "/mutant/" endpoint.
    """
    dna: List[str]

    class Config:
        orm_mode = True


class DnaAnalysis(BaseModel):
    """
    DnaAnalysis model. Represent DnaAnalysis database model class.
    """
    id: int
    dna_hash: str
    analysis_date: datetime
    is_mutant: bool

    class Config:
        orm_mode = True


class DnaStats(BaseModel):
    """
    DnaStats model. Object for "/stats/" endpoint.
    """
    count_mutant_dna: int
    count_human_dna: int
    ratio: float
