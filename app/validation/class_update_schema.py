from marshmallow import fields, validates_schema, ValidationError
from .base_schema import BaseSchema
from ..models.class_model import ClassModel


class ClassUpdateSchema(BaseSchema):
    id = fields.Int()
    name = fields.Str()

    @validates_schema
    def class_name_is_exists(self, data, **kwargs):
        if data['id'] is not None:
            class_instance = ClassModel.query.filter(ClassModel.name == data['name'], ClassModel.id != data['id']).first()
        else:
            class_instance = ClassModel.query.filter(ClassModel.name == data['name']).first()
        
        if class_instance:
            raise ValidationError('Name already exists')
