from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, func
from .session import Base 

class RunLog(Base):
    __tablename__ = "run_logs"

    id = Column(Integer, primary_key=True)
    url = Column(String(2048))
    task_type = Column(String(64))
    model = Column(String(64))
    output_text = Column(Text)
    toxicity = Column(Float, default=0.0)
    flagged = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
