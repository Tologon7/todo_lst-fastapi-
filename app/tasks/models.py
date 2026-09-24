from app.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey
from datetime import datetime, timezone

from app.users.models import Users


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    name = Column(String, nullable=False)
    description = Column(Text)
    complexity = Column(Integer, default=1)
    data_create = Column(Date, default=datetime.now(timezone.utc))
    deadline = Column(Date)
    done = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
