from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import teacher_permission
from app.principle import student_permission
from ..services.scenario_practice_service import ScenarioPracticeService
from ..validation.scenario_practice_index_schema import ScenarioPracticeIndexSchema
from ..validation.scenario_practice_store_schema import ScenarioPracticeStoreSchema
from ..validation.char_data_get_schema import CharDataGetSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

scenario_practice_blueprint = Blueprint(
    'scenario_practice_blueprint', __name__)
scenario_practice_service = ScenarioPracticeService()


@scenario_practice_blueprint.route('/scenario_practices/list', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def get_all_quantity_limited_practices():
    try:
        response, total = scenario_practice_service.get_all_scenario_practices()
        return make_success_response(
            data=response,
            status_code=200,
            total=total,
        )
    except Exception as e:
        return make_error_response(e, 500)


@scenario_practice_blueprint.route('/scenario_practices', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def index():
    messages = []

    try:
        validated_data = ScenarioPracticeIndexSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response, max_page, total, from_index, to_index = scenario_practice_service.get_scenario_practices(
            name=validated_data.get('name'),
            class_id_list=validated_data.get('class_id_list'),
            scenario_id_list=validated_data.get('scenario_id_list'),
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


@scenario_practice_blueprint.route('/scenario_practices/chart/users/<int:user_id>', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def get_scenario_practices_chart_data(user_id):
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
        response = scenario_practice_service.get_scenario_practices_chart_data(
            user_id=validated_data.get('user_id'),
            finished_start=validated_data.get('finished_start'),
            finished_end=validated_data.get('finished_end'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@scenario_practice_blueprint.route('/scenario_practices', methods=['POST'])
@student_permission.require(http_exception=403)
@login_required
def store():
    data = request.json
    messages = []

    try:
        validated_data = ScenarioPracticeStoreSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = scenario_practice_service.insert_scenario_practice(
            user_id=validated_data.get('user_id'),
            scenario_id=validated_data.get('scenario_id'),
            level1_time=validated_data.get('level1_time'),
            level2_time=validated_data.get('level2_time'),
            level3_time=validated_data.get('level3_time'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)
