from marshmallow import fields
from .base_schema import BaseSchema


class ClassStoreSchema(BaseSchema):
    name = fields.Str(validate=BaseSchema.class_name_exists)
