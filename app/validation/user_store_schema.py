from marshmallow import fields, validate
from .base_schema import BaseSchema


class UserStoreSchema(BaseSchema):
    class_id = fields.Int(validate=BaseSchema.class_id_not_exists)
    name = fields.Str(validate=validate.Length(min=1))
    account = fields.Str(
        validate=(BaseSchema.user_account_exists))
