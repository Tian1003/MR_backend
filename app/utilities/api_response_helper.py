from flask import jsonify


def make_success_response(data, status_code, total=None, from_index=None, to_index=None, current_page=None, per_page=None, max_page=None):
    response = {
        "data": data,
        "total": total if total else 1,
        "messages": None,
        "status": "success",
    }

    if current_page is not None:
        response["current_page"] = current_page
    if per_page is not None:
        response["per_page"] = per_page
    if max_page is not None:
        response["max_page"] = max_page
    if from_index is not None:
        response["from"] = from_index
    if to_index is not None:
        response["to"] = to_index

    return jsonify(response), status_code


def make_error_response(messages, status_code):
    response = {
        "data": None,
        "messages": messages,
        "status": "error",
    }
    return jsonify(response), status_code
