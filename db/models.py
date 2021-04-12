from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime

from db.database import Base


class DnaAnalysis(Base):
    """
    DnaAnalysis model class for dna_analysis database table.
    Store every unexisting analysis processed by the API.
    """
    __tablename__ = "dna_analysis"

    id = Column(Integer, primary_key=True, index=True)
    dna_hash = Column(String, unique=True, index=True)
    dna = Column(Text)
    analysis_date = Column(DateTime, default=datetime.now)
    is_mutant = Column(Boolean, default=False)
