from marshmallow import fields, validates_schema, ValidationError
from .base_schema import BaseSchema
from ..models.quantity_limited_practice_model import QuantityLimitedPracticeModel
from ..models.quantity_limited_test_model import QuantityLimitedTestModel
from ..models.time_limited_practice_model import TimeLimitedPracticeModel
from ..models.time_limited_test_model import TimeLimitedTestModel

class AnswerDetailGetSchema(BaseSchema):
    record_id = fields.Int(required=True)
    question_type = fields.Str(required=True)
    level = fields.Int(required=True)

    @validates_schema
    def question_type_is_exists(self, data, **kwargs):
        print(data['question_type'])
        if data['question_type'] not in ["quantity_limited_practices", "quantity_limited_tests", "time_limited_practices", "time_limited_tests"]:
            raise ValidationError('question_type not found')

    @validates_schema
    def record_id_is_exists(self, data, **kwargs):
        print(data['record_id'])
        if data['question_type'] == "quantity_limited_practices":
            query = QuantityLimitedPracticeModel.query.filter(QuantityLimitedPracticeModel.id == data['record_id'])
        elif data['question_type'] == "quantity_limited_tests":
            query = QuantityLimitedTestModel.query.filter(QuantityLimitedTestModel.id == data['record_id'])
        elif data['question_type'] == "time_limited_practices":
            query = TimeLimitedPracticeModel.query.filter(TimeLimitedPracticeModel.id == data['record_id'])
        elif data['question_type'] == "time_limited_tests":
            query = TimeLimitedTestModel.query.filter(TimeLimitedTestModel.id == data['record_id'])

        result = query.first()

        if not result:
            raise ValidationError('Record not found')