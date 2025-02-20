from marshmallow import fields
from .base_schema import BaseSchema


class ClassIndexSchema(BaseSchema):
    name = fields.Str()
