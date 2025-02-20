from marshmallow import fields
from .base_schema import BaseSchema


class QuantityLimitedTestUpdateSchema(BaseSchema):
    id = fields.Int(
        required=True, validate=BaseSchema.quantity_limited_test_id_not_exists)
    level = fields.Int(
        required=True, validate=BaseSchema.validate_level)
    correct_quantity = fields.Int(required=True, )
    total_quantity = fields.Int(required=True, )
    time = fields.Int(required=True, )
    answer_detail = fields.List(fields.Dict(), required=True)
