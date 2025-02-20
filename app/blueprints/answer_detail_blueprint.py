from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import teacher_or_student_permission
from ..services.answer_detail_service import AnswerDetailService
from ..validation.answer_detail_get_schema import AnswerDetailGetSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

answer_detail_blueprint = Blueprint('answer_detail_blueprint', __name__)
answer_detail_service = AnswerDetailService()


@answer_detail_blueprint.route('/answer_details', methods=['GET'])
@teacher_or_student_permission.require(http_exception=403)
@login_required
def get_answer_detail():
    messages = []
    try:
        validated_data = AnswerDetailGetSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response, total = answer_detail_service.get_answer_detail(
            record_id=validated_data.get('record_id'),
            question_type=validated_data.get('question_type'),
            level=validated_data.get('level'),
        )
        return make_success_response(response, 200, total)
    except Exception as e:
        return make_error_response(e, 500)
