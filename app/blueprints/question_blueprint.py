from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import student_permission
from ..services.level_service import LevelService
from ..validation.level_data_get_schema import LevelDataGetSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

question_blueprint = Blueprint('question_blueprint', __name__)
level_service = LevelService()


@question_blueprint.route('/questions', methods=['GET'])
@student_permission.require(http_exception=403)
@login_required
def get_level_data():
    messages = []

    try:
        validated_data = LevelDataGetSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response, total = level_service.get_level_data(
            type_id=validated_data.get('type_id'),
            level=validated_data.get('level'),
        )
        return make_success_response(response, 200, total)
    except Exception as e:
        return make_error_response(e, 500)
