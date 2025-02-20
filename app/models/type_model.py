from sqlalchemy import Column, Integer, String
from .base_model import BaseModel


class TypeModel(BaseModel):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
