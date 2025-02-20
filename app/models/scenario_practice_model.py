from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .user_model import UserModel
from .scenario_model import ScenarioModel


class ScenarioPracticeModel(BaseModel):
    __tablename__ = "scenario_practices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), nullable=False)
    level1_time = Column(Integer, nullable=False)
    level2_time = Column(Integer, nullable=True)
    level3_time = Column(Integer, nullable=True)
    finished_at = Column(TIMESTAMP, nullable=False)

    # user = relationship(UserModel, backref='users')
    scenario = relationship(ScenarioModel)

    def __init__(self, id=None, user_id=None, scenario_id=None, level1_time=None, level2_time=None, level3_time=None, finished_at=None):
        self.id = id
        self.user_id = user_id
        self.scenario_id = scenario_id
        self.level1_time = level1_time
        self.level2_time = level2_time
        self.level3_time = level3_time
        self.finished_at = finished_at
