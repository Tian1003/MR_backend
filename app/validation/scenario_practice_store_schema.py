from marshmallow import fields
from .base_schema import BaseSchema


class ScenarioPracticeStoreSchema(BaseSchema):
    user_id = fields.Int(
        required=True, validate=BaseSchema.user_id_not_exists)
    scenario_id = fields.Int(
        required=True, validate=BaseSchema.scenario_id_not_exists)
    level1_time = fields.Int(required=True, )
    level2_time = fields.Int(required=True, )
    level3_time = fields.Int(required=True, )
