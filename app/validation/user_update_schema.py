from marshmallow import fields, validate, validates_schema, ValidationError
from .base_schema import BaseSchema
from ..models.user_model import UserModel

class UserUpdateSchema(BaseSchema):
    id = fields.Int(validate=BaseSchema.user_id_not_exists)
    class_id = fields.Int(validate=BaseSchema.class_id_not_exists)
    account = fields.Str()
    name = fields.Str(validate=validate.Length(min=1))

    @validates_schema
    def user_account_is_exists(self, data, **kwargs):
        user = UserModel.query.filter(UserModel.account == data['account'], UserModel.id != data['id']).first()
        
        if user:
            raise ValidationError('Account already exists')
