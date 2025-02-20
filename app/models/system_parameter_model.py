from sqlalchemy import Column, Integer, String
from .base_model import BaseModel


class SystemParameterModel(BaseModel):
    __tablename__ = "system_parameters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)

    def __init__(self, id=None, key=None, value=None):
        self.id = id
        self.key = key
        self.value = value
