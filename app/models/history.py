from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)

    operation = Column(String, nullable=False)

    number1 = Column(Float, nullable=False)

    number2 = Column(Float, nullable=True)

    result = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")