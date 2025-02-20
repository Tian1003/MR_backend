from marshmallow import fields
from .base_schema import BaseSchema


class UserShowSchema(BaseSchema):
    id = fields.Int(validate=BaseSchema.user_id_not_exists)
