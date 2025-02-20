from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/unit/class_update.feature')


@given(
    parsers.parse(
        'name 欄位 {name}'),
    target_fixture='given_valid_parameters',
    converters={
        'name': str
    }
)
def given_valid_parameters(name):
    return {
        "name": name
    }


def get_session_value(client):
    login_data = {
        'account': 'teacher',
        'password': 'teacher'
    }
    login_response = client.post(
        '/api/teacher/login', json=login_data, content_type='application/json')
    session_cookie = login_response.headers.get('Set-Cookie')
    if session_cookie:
        session_value = session_cookie.split(';')[0].split('=')[1]
        return session_value
    else:
        return None


@when(
    parsers.parse('發送 update 請求至後端 endpoint /api/classes/{id}'),
    target_fixture='when_send_update_request',
    converters={
        'id': int,
    }
)
def when_send_update_request(client, given_valid_parameters, id):
    headers = {
        'Cookie': f'session={get_session_value(client)}'
    }
    response = client.patch(f'/api/classes/{id}', json=given_valid_parameters,
                            content_type='application/json', headers=headers)
    return response


@then('返回 status code 200;\ndata 欄位包含 id, name;\nmessages 欄位值為 null;\nstatus 欄位值為 "success"\ntotal 欄位值不為 0')
def then_check_response(when_send_update_request):
    json_response = when_send_update_request.get_json()
    assert when_send_update_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('messages') is None
    assert json_response.get('data').get('id') is not None
    assert json_response.get('data').get('name') is not None
