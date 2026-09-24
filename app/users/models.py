from app.database import Base
from sqlalchemy import Column, Integer, Date, Boolean, String, ForeignKey
from datetime import datetime, timezone

from app.users.roles.models import Role


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    data_create = Column(Date, default=datetime.now(timezone.utc))
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(ForeignKey("roles.id"), default=1)
