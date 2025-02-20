from marshmallow import fields
from .base_schema import BaseSchema


class QuantityLimitedTestStoreSchema(BaseSchema):
    user_id = fields.Int(
        required=True, validate=BaseSchema.user_id_not_exists)
    type_id = fields.Int(
        required=True, validate=BaseSchema.type_id_not_exists)
    correct_quantity = fields.Int(required=True, )
    total_quantity = fields.Int(required=True, )
    time = fields.Int(required=True, )
    answer_detail = fields.List(fields.Dict(), required=True)
