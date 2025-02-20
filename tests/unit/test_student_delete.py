from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/unit/student_delete.feature')


@given(
    parsers.parse(
        'user_id 欄位 {id}'),
    target_fixture='given_valid_parameters',
    converters={
        'id': int,
    }
)
def given_valid_parameters(id):
    assert id in [3, 4]


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
    parsers.parse('發送 delete 請求至後端 endpoint /api/students/{id}'),
    target_fixture='when_send_insert_request',
    converters={
        'class_id': int,
    }
)
def when_send_insert_request(client, id):
    headers = {
        'Cookie': f'session={get_session_value(client)}'
    }
    response = client.delete(
        f'/api/students/{id}', content_type='application/json', headers=headers)
    return response


@then('返回 status code 200;\nmessages 欄位值為 null;\nstatus 欄位值為 "success"')
def then_check_response(when_send_insert_request):
    json_response = when_send_insert_request.get_json()
    assert when_send_insert_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('messages') is None
    assert json_response.get('data') is None
