from marshmallow import fields, ValidationError
from .base_schema import BaseSchema


def validate_not_admin(value):
    if value.lower() == "teacher" or value.lower() == "developer":
        raise ValidationError("Account not found")


class StudentLoginSchema(BaseSchema):
    account = fields.Str(
        required=True, validate=[BaseSchema.user_account_not_exists, validate_not_admin]
    )
