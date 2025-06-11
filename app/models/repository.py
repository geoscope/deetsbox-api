import uuid
from app.models.base import Base
from sqlalchemy import Column, String, create_engine, Field
from sqlalchemy.orm import sessionmaker


class Repository(Base):
    __tablename__ = "repositories"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name = Column(String, index=True, length=256)
