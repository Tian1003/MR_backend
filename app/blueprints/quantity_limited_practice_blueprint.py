from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import teacher_permission
from app.principle import student_permission
from app.principle import teacher_or_student_permission
from ..services.quantity_limited_practice_service import QuantityLimitedPracticeService
from ..validation.record_index_schema import RecordIndexSchema
from ..validation.quantity_limited_practice_store_schema import QuantityLimitedPracticeStoreSchema
from ..validation.quantity_limited_practice_update_schema import QuantityLimitedPracticeUpdateSchema
from ..validation.char_data_get_schema import CharDataGetSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

quantity_limited_practice_blueprint = Blueprint(
    'quantity_limited_practice_blueprint', __name__)
quantity_limited_practice_service = QuantityLimitedPracticeService()


@quantity_limited_practice_blueprint.route('/quantity_limited_practices/list', methods=['GET'])
@teacher_or_student_permission.require(http_exception=403)
@login_required
def get_all_quantity_limited_practices():
    try:
        user_id = request.args.get('user_id')
        response, total = quantity_limited_practice_service.get_all_quantity_limited_practices(
            user_id=user_id
        )
        return make_success_response(
            data=response,
            status_code=200,
            total=total,
        )
    except Exception as e:
        return make_error_response(e, 500)


@quantity_limited_practice_blueprint.route('/quantity_limited_practices/rank_list', methods=['GET'])
@student_permission.require(http_exception=403)
@login_required
def get_quantity_limited_practices_rank_list():
    try:
        response, total = quantity_limited_practice_service.get_quantity_limited_practices_rank_list()
        return make_success_response(
            data=response,
            status_code=200,
            total=total,
        )
    except Exception as e:
        return make_error_response(e, 500)


@quantity_limited_practice_blueprint.route('/quantity_limited_practices', methods=['GET'])
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
        response, max_page, total, from_index, to_index = quantity_limited_practice_service.get_quantity_limited_practices(
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


@quantity_limited_practice_blueprint.route('/quantity_limited_practices/chart/users/<int:user_id>', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def get_quantity_limited_practices_chart_data(user_id):
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
        response = quantity_limited_practice_service.get_quantity_limited_practices_chart_data(
            user_id=validated_data.get('user_id'),
            finished_start=validated_data.get('finished_start'),
            finished_end=validated_data.get('finished_end'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@quantity_limited_practice_blueprint.route('/quantity_limited_practices', methods=['POST'])
@student_permission.require(http_exception=403)
@login_required
def store():
    data = request.json
    messages = []

    try:
        validated_data = QuantityLimㄈitedPracticeStoreSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = quantity_limited_practice_service.insert_quantity_limited_practice(
            user_id=validated_data.get('user_id'),
            type_id=validated_data.get('type_id'),
            level=1,
            total_quantity=validated_data.get('total_quantity'),
            time=validated_data.get('time'),
            answer_detail=validated_data.get('answer_detail'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@quantity_limited_practice_blueprint.route('/quantity_limited_practices/<int:id>/level/<int:level>', methods=['PATCH'])
@student_permission.require(http_exception=403)
@login_required
def update(id, level):
    data = request.json
    data["id"] = id
    data["level"] = level
    messages = []

    try:
        validated_data = QuantityLimitedPracticeUpdateSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = quantity_limited_practice_service.update_quantity_limited_practice(
            id=validated_data.get('id'),
            level=validated_data.get('level'),
            total_quantity=validated_data.get('total_quantity'),
            time=validated_data.get('time'),
            answer_detail=validated_data.get('answer_detail'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)
