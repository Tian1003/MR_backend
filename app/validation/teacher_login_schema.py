from marshmallow import Schema, fields, ValidationError, validates_schema
from ..models.user_model import UserModel


def validate_account(account):
    user = UserModel.query.filter(UserModel.account == account).first()
    if not user:
        raise ValidationError('Account not found')


class TeacherLoginSchema(Schema):
    account = fields.Str(required=True, validate=validate_account)
    password = fields.Str(required=True)
