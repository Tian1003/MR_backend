from marshmallow import fields
from .base_schema import BaseSchema


class ClassDeleteSchema(BaseSchema):
    id = fields.Int(validate=BaseSchema.class_id_not_exists)
