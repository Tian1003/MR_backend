from marshmallow import fields
from .base_schema import BaseSchema


class TimeLimitedTestStoreSchema(BaseSchema):
    user_id = fields.Int(
        required=True, validate=BaseSchema.user_id_not_exists)
    type_id = fields.Int(
        required=True, validate=BaseSchema.type_id_not_exists)
    total_quantity = fields.Int(required=True, )
    correct_quantity = fields.Int(required=True, )
    incorrect_quantity = fields.Int(required=True, )
    time = fields.Int(required=True, )
    time_limit = fields.Int(required=True, )
    answer_detail = fields.List(fields.Dict(), required=True)
