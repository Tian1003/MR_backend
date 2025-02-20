from sqlalchemy import Column, Integer, String, ForeignKey
from .base_model import BaseModel
from .question_model import QuestionModel
from sqlalchemy.orm import relationship

class AnswerDetailModel(BaseModel):
    __tablename__ = 'answer_details'
    id = Column(Integer, primary_key=True)
    record_id = Column(Integer, index=True, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    question_type = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    selected_mixed_number = Column(Integer, nullable=True)
    selected_numerator = Column(Integer, nullable=True)
    selected_denominator = Column(Integer, nullable=True)
    selected_operator = Column(String(2), nullable=True)

    question = relationship(QuestionModel, backref='questions')