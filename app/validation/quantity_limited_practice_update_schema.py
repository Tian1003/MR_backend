from marshmallow import fields
from .base_schema import BaseSchema


class QuantityLimitedPracticeUpdateSchema(BaseSchema):
    id = fields.Int(
        required=True, validate=BaseSchema.quantity_limited_practice_id_not_exists)
    level = fields.Int(
        required=True, validate=BaseSchema.validate_level)
    total_quantity = fields.Int(required=True, )
    time = fields.Int(required=True, )
    answer_detail = fields.List(fields.Dict(), required=True)
