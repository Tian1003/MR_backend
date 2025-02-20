from marshmallow import fields
from .base_schema import BaseSchema


class TimeLimitedPracticeUpdateSchema(BaseSchema):
    id = fields.Int(
        required=True, validate=BaseSchema.time_limited_practice_id_not_exists)
    level = fields.Int(
        required=True, validate=BaseSchema.validate_level)
    correct_quantity = fields.Int(required=True, )
    total_quantity = fields.Int(required=True, )
    time = fields.Int(required=True, )
    time_limit = fields.Int(required=True, )
    answer_detail = fields.List(fields.Dict(), required=True)
