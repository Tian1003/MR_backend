from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .scenario_element_model import ScenarioElementModel

class ScenarioQuestionModel(BaseModel):
    __tablename__ = "scenario_questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    scenario_element_id = Column(Integer, ForeignKey('scenario_elements.id'), nullable=False)
    mixed_number = Column(Integer, nullable=True) #帶分整數
    numerator = Column(Integer, nullable=True)
    denominator = Column(Integer, nullable=True)

    scenario_element = relationship(ScenarioElementModel, backref='scenario_elements')

    def __init__(self, id=None, scenario_element_id=None, mixed_number=None, numerator=None, denominator=None):
        self.id = id
        self.scenario_element_id = scenario_element_id
        self.mixed_number = mixed_number
        self.numerator = numerator
        self.denominator = denominator
