from flask import Blueprint, request
from flask_login import login_required
from marshmallow import ValidationError
from app.principle import teacher_permission
from ..services.class_service import ClassService
from ..validation.class_index_schema import ClassIndexSchema
from ..validation.class_store_schema import ClassStoreSchema
from ..validation.class_update_schema import ClassUpdateSchema
from ..validation.class_delete_schema import ClassDeleteSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

class_blueprint = Blueprint('class_blueprint', __name__)
class_service = ClassService()


@class_blueprint.route('/classes', methods=['GET'])
def index():
    messages = []

    try:
        validated_data = ClassIndexSchema().load(request.args.to_dict())
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = class_service.get_classes(
            name=validated_data.get('name'),
        )
        return make_success_response(response, 200, len(response))
    except Exception as e:
        return make_error_response(e, 500)


@class_blueprint.route('/classes', methods=['POST'])
@teacher_permission.require(http_exception=403)
@login_required
def store():
    data = request.json
    messages = []

    try:
        validated_data = ClassStoreSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = class_service.insert_class(
            name=validated_data.get('name'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@class_blueprint.route('/classes/<int:id>', methods=['PATCH'])
@teacher_permission.require(http_exception=403)
@login_required
def update(id):
    data = request.json
    data["id"] = id
    messages = []

    try:
        validated_data = ClassUpdateSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = class_service.update_class(
            id=validated_data.get('id'),
            name=validated_data.get('name'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        return make_error_response(e, 500)


@class_blueprint.route('/classes/<int:id>', methods=['DELETE'])
@teacher_permission.require(http_exception=403)
@login_required
def delete(id):
    messages = []

    try:
        validated_data = ClassDeleteSchema().load({
            "id": id
        })
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    try:
        response = class_service.delete_class(
            id=validated_data.get('id'),
        )
        return make_success_response(response, 200)
    except Exception as e:
        print(e)
        return make_error_response(e, 500)
