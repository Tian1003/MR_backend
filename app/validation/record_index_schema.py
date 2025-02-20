from marshmallow import fields
from .base_schema import BaseSchema


class RecordIndexSchema(BaseSchema):
    name = fields.Str()
    class_id_list = fields.Str(validate=BaseSchema.class_id_list_not_exists)
    type_id_list = fields.Str(validate=BaseSchema.type_id_list_not_exists)
    finished_start = fields.Date(format='%Y-%m-%d')
    finished_end = fields.Date(format='%Y-%m-%d')
    page = fields.Int(required=True)
    per_page = fields.Int(required=True)
