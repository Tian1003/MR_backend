from marshmallow import fields
from .base_schema import BaseSchema


class LevelDataGetSchema(BaseSchema):
    type_id = fields.Int(
        required=True, validate=BaseSchema.type_id_not_exists)
    level = fields.Int(
        required=True, validate=BaseSchema.validate_level)
