from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class ClassModel(BaseModel):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    users = relationship(
        'UserModel',
        back_populates='class_instance',
        foreign_keys='UserModel.class_id',
        cascade='all, delete-orphan'
    )

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
