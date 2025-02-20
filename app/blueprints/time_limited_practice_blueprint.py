from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import teacher_permission
from app.principle import student_permission
from app.principle import teacher_or_student_permission
from app.validation.char_data_get_schema import CharDataGetSchema
from app.validation.record_index_schema import RecordIndexSchema
from ..services.time_limited_practice_service import TimeLimitedPracticeService
from ..validation.time_limited_practice_store_schema import TimeLimitedPracticeStoreSchema
from ..validation.time_limited_practice_update_schema import TimeLimitedPracticeUpdateSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

time_limited_practice_blueprint = Blueprint(
    'time_limited_practice_blueprint', __name__)
time_limited_practice_service = TimeLimitedPracticeService()


@time_limited_practice_blueprint.route('/time_limited_practices/list', methods=['GET'])
@teacher_or_student_permission.require(http_exception=403)
@login_required
def get_all_time_limited_practices():
    try:
        user_id = request.args.get('user_id')
        response, total = time_limited_practice_service.get_all_time_limited_practices(
            user_id=user_id
        )
        return make_success_response(
            data=response,
            status_code=200,
            total=total,
        )
    except Exception as e:
        return make_error_response(e, 500)


@time_limited_practice_blueprint.route('/time_limited_practices/rank_list', methods=['GET'])
@student_permission.require(http_exception=403)
@login_required
def get_time_limited_practices_rank_list():
    try:
        response, total = time_limited_practice_service.get_time_limited_practices_rank_list()
        return make_success_response(
            data=response,
            status_code=200,
            total=total,
        )
    except Exception as e:
        return make_error_response(e, 500)


@time_limited_practice_blueprint.route('/time_limited_practices', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def index():
    messages = []

    try:
        validated_data = RecordIndexSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response, max_page, total, from_index, to_index = time_limited_practice_service.get_time_limited_practices(
            name=validated_data.get('name'),
            class_id_list=validated_data.get('class_id_list'),
            type_id_list=validated_data.get('type_id_list'),
            finished_start=validated_data.get('finished_start'),
            finished_end=validated_data.get('finished_end'),
            page=validated_data.get('page'),
            per_page=validated_data.get('per_page'),
        )
        return make_success_response(
            data=response,
            status_code=200,
            total=total,
            from_index=from_index,
            to_index=to_index,
            current_page=validated_data.get('page'),
            per_page=validated_data.get('per_page'),
            max_page=max_page,
        )
    except Exception as e:
        return make_error_response(e, 500)


@time_limited_practice_blueprint.route('/time_limited_practices/chart/users/<int:user_id>', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def get_time_limited_practices_chart_data(user_id):
    messages = []

    try:
        validated_data = CharDataGetSchema().load({
            'user_id': user_id,
            **request.args.to_dict()
        })
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = time_limited_practice_service.get_time_limited_practice_chart_data(
            user_id=validated_data.get('user_id'),
            finished_start=validated_data.get('finished_start'),
            finished_end=validated_data.get('finished_end'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@time_limited_practice_blueprint.route('/time_limited_practices', methods=['POST'])
@student_permission.require(http_exception=403)
@login_required
def store():
    data = request.json
    messages = []

    try:
        validated_data = TimeLimitedPracticeStoreSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = time_limited_practice_service.insert_time_limited_practice(
            user_id=validated_data.get('user_id'),
            type_id=validated_data.get('type_id'),
            level=1,
            total_quantity=validated_data.get('total_quantity'),
            correct_quantity=validated_data.get('correct_quantity'),
            time=validated_data.get('time'),
            time_limit=validated_data.get('time_limit'),
            answer_detail=validated_data.get('answer_detail'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@time_limited_practice_blueprint.route('/time_limited_practices/<int:id>/level/<int:level>', methods=['PATCH'])
@student_permission.require(http_exception=403)
@login_required
def update(id, level):
    data = request.json
    data["id"] = id
    data["level"] = level

    messages = []

    try:
        validated_data = TimeLimitedPracticeUpdateSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = time_limited_practice_service.update_time_limited_practice(
            id=validated_data.get('id'),
            level=validated_data.get('level'),
            total_quantity=validated_data.get('total_quantity'),
            correct_quantity=validated_data.get('correct_quantity'),
            time=validated_data.get('time'),
            time_limit=validated_data.get('time_limit'),
            answer_detail=validated_data.get('answer_detail'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)
