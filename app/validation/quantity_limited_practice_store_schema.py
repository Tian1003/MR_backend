from marshmallow import fields
from .base_schema import BaseSchema


class QuantityLimitedPracticeStoreSchema(BaseSchema):
    user_id = fields.Int(
        required=True, validate=BaseSchema.user_id_not_exists)
    type_id = fields.Int(
        required=True, validate=BaseSchema.type_id_not_exists)
    total_quantity = fields.Int(required=True, )
    time = fields.Int(required=True, )
    answer_detail = fields.List(fields.Dict(), required=True)
    # selected_mixed_number = fields.Int(required=False, allow_none=True)
    # selected_numerator = fields.Int(required=True, )
    # selected_denominator = fields.Int(required=True, )
