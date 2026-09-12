from app.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, Date
from datetime import datetime, timezone

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    complexity = Column(Integer)
    data_create = Column(Date, default=datetime.now(timezone.utc))
    deadline = Column(Date)
    is_active = Column(Boolean, default=True)
