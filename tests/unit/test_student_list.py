from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/unit/student_list.feature')


@given(
    parsers.parse(
        'class_id_list 欄位 {class_id_list}'),
    target_fixture='given_valid_parameters',
    converters={
        'class_id_list': str,
    }
)
def given_valid_parameters(class_id_list):
    assert '1' in class_id_list or '2' in class_id_list

    return {
        "class_id_list": class_id_list,
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


@when("發送 get 請求至後端 endpoint /api/students", target_fixture='when_send_get_list_request')
def when_send_get_list_request(client, given_valid_parameters):
    headers = {
        'Cookie': f'session={get_session_value(client)}'
    }
    response = client.get('/api/students', json=given_valid_parameters,
                          content_type='application/json', headers=headers)
    return response


@then('返回 status code 200;\ndata 欄位包含 id, account, name, class_;\n    class_ 欄位包含 id, name;\nmessages 欄位值為 null;\nstatus 欄位值為 "success"\ntotal 欄位值不為 0')
def then_check_response(when_send_get_list_request):
    json_response = when_send_get_list_request.get_json()
    result = list(json_response.get('data'))
    assert when_send_get_list_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('messages') is None
    assert result is not None
    assert result[0]['id'] is not None
    assert result[0]['account'] is not None
    assert result[0]['name'] is not None
    assert result[0]['class_'] is not None
    assert result[0]['class_']['id'] is not None
    assert result[0]['class_']['name'] is not None
