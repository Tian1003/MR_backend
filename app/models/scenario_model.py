from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class ScenarioModel(BaseModel):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
