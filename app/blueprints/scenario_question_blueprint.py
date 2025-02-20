from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import student_permission
from ..services.scenario_level_service import ScenarioLevelService
from ..validation.scenario_level_data_get_schema import ScenarioLevelDataGetSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

scenario_question_blueprint = Blueprint('scenario_question_blueprint', __name__)
scenario_level_service = ScenarioLevelService()

@scenario_question_blueprint.route('/scenario_questions', methods=['GET'])
@student_permission.require(http_exception=403)
@login_required
def get_level_data():
    messages = []

    try:
        validated_data = ScenarioLevelDataGetSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response, total = scenario_level_service.get_scenario_level_data(
            scenario_id=validated_data.get('scenario_id'),
            level=validated_data.get('level'),
        )
        return make_success_response(response, 200, total)
    except Exception as e:
        return make_error_response(e, 500)
