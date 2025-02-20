from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .type_model import TypeModel


class QuestionModel(BaseModel):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=False)
    first_mixed_number = Column(Integer, nullable=True)
    first_numerator = Column(Integer, nullable=True)
    first_denominator = Column(Integer, nullable=True)
    operator = Column(String(2), nullable=False)
    second_mixed_number = Column(Integer, nullable=True)
    second_numerator = Column(Integer, nullable=True)
    second_denominator = Column(Integer, nullable=True)
    answer_mixed_number = Column(Integer, nullable=True)
    answer_numerator = Column(Integer, nullable=True)
    answer_denominator = Column(Integer, nullable=True)
    options = Column(JSON, nullable=False)

    type = relationship(TypeModel, backref='questions')

    def __init__(self, type_id, first_mixed_number, first_numerator, first_denominator, operator, second_mixed_number, second_numerator, second_denominator, answer_mixed_number, answer_numerator, answer_denominator, options):
        self.type_id = type_id
        self.first_mixed_number = first_mixed_number
        self.first_numerator = first_numerator
        self.first_denominator = first_denominator
        self.operator = operator
        self.second_mixed_number = second_mixed_number
        self.second_numerator = second_numerator
        self.second_denominator = second_denominator
        self.answer_mixed_number = answer_mixed_number
        self.answer_numerator = answer_numerator
        self.answer_denominator = answer_denominator
        self.options = options
