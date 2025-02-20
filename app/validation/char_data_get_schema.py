from marshmallow import fields
from .base_schema import BaseSchema


class CharDataGetSchema(BaseSchema):
    user_id = fields.Int(
        required=True, validate=BaseSchema.user_id_not_exists)
    finished_start = fields.Date(format='%Y-%m-%d')
    finished_end = fields.Date(format='%Y-%m-%d')
