from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .scenario_model import ScenarioModel

class ScenarioElementModel(BaseModel):
    __tablename__ = "scenario_elements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), nullable=False)
    level = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)

    scenario = relationship(ScenarioModel, backref='scenarios')

    def __init__(self, id=None, scenario_id=None, level=None, name=None):
        self.id = id
        self.scenario_id = scenario_id
        self.level = level
        self.name = name
