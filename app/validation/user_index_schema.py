from marshmallow import fields
from .base_schema import BaseSchema


class UserIndexSchema(BaseSchema):
    name = fields.Str()
    account = fields.Str()
    class_id_list = fields.Str(validate=BaseSchema.class_id_list_not_exists)
