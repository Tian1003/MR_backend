from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from flask_login import UserMixin


class UserModel(BaseModel, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey('classes.id'), nullable=True)
    account = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    password = Column(String(60), nullable=True)

    class_instance = relationship(
        'ClassModel', back_populates='users', foreign_keys='[UserModel.class_id]')
    quantity_limited_practices = relationship(
        'QuantityLimitedPracticeModel',
        backref='user',
        cascade='all, delete-orphan'
    )
    quantity_limited_tests = relationship(
        'QuantityLimitedTestModel',
        backref='user',
        cascade='all, delete-orphan'
    )
    time_limited_practices = relationship(
        'TimeLimitedPracticeModel',
        backref='user',
        cascade='all, delete-orphan'
    )
    time_limited_tests = relationship(
        'TimeLimitedTestModel',
        backref='user',
        cascade='all, delete-orphan'
    )
    scenario_practices = relationship(
        'ScenarioPracticeModel',
        backref='user',
        cascade='all, delete-orphan'
    )

    def __init__(self, id=None, class_id=None, account=None, name=None, password=None):
        self.id = id
        self.class_id = class_id
        self.account = account
        self.name = name
        self.password = password
