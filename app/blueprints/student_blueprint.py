from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import teacher_permission
from ..services.user_service import UserService
from ..validation.user_index_schema import UserIndexSchema
from ..validation.user_store_schema import UserStoreSchema
from ..validation.user_show_schema import UserShowSchema
from ..validation.user_update_schema import UserUpdateSchema
from ..utilities.api_response_helper import make_success_response, make_error_response


student_blueprint = Blueprint('student_blueprint', __name__)
user_service = UserService()


@student_blueprint.route('/students', methods=['GET'])
@login_required
def index():
    messages = []

    try:
        validated_data = UserIndexSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response, total = user_service.get_users(
            name=validated_data.get('name'),
            account=validated_data.get('account'),
            class_id_list=validated_data.get('class_id_list'),
        )
        return make_success_response(response, 200, total)
    except Exception as e:
        return make_error_response(e, 500)


@student_blueprint.route('/students', methods=['POST'])
@teacher_permission.require(http_exception=403)
@login_required
def store():
    data = request.json
    messages = []

    try:
        validated_data = UserStoreSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = user_service.insert_user(
            name=validated_data.get('name'),
            account=validated_data.get('account'),
            class_id=validated_data.get('class_id'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@student_blueprint.route('/students/<int:id>', methods=['GET'])
@teacher_permission.require(http_exception=403)
@login_required
def show(id):
    messages = []

    try:
        validated_data = UserShowSchema().load({
            "id": id
        })
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = user_service.get_user(
            id=validated_data.get('id'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@student_blueprint.route('/students/<int:id>', methods=['PATCH'])
@teacher_permission.require(http_exception=403)
@login_required
def update(id):
    data = request.json
    data["id"] = id
    messages = []

    try:
        validated_data = UserUpdateSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = user_service.update_user(
            id=validated_data.get('id'),
            class_id=validated_data.get('class_id'),
            account=validated_data.get('account'),
            name=validated_data.get('name'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@student_blueprint.route('/students/<int:id>', methods=['DELETE'])
@teacher_permission.require(http_exception=403)
@login_required
def delete(id):
    messages = []

    try:
        validated_data = UserShowSchema().load({
            "id": id
        })
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = user_service.delete_user(
            id=validated_data.get('id'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)
