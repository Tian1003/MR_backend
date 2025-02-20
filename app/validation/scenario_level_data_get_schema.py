from marshmallow import fields
from .base_schema import BaseSchema


class ScenarioLevelDataGetSchema(BaseSchema):
    scenario_id = fields.Int(
        required=True, validate=BaseSchema.scenario_id_not_exists)
    level = fields.Int(
        required=True, validate=BaseSchema.validate_level)
