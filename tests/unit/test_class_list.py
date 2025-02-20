from pytest_bdd import scenarios, when, then


scenarios('../features/unit/class_list.feature')


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


@when("發送 get 請求至後端 endpoint /api/classes", target_fixture='when_send_get_list_request')
def when_send_get_list_request(client):
    headers = {
        'Cookie': f'session={get_session_value(client)}'
    }
    response = client.get('/api/classes', json="",
                          content_type='application/json', headers=headers)
    return response


@then('返回 status code 200;\ndata 欄位包含 id, name, users;\n    users 欄位包含 id, account, name;\nmessages 欄位值為 null;\nstatus 欄位值為 "success"\ntotal 欄位值不為 0')
def then_check_response(when_send_get_list_request):
    json_response = when_send_get_list_request.get_json()
    result = list(json_response.get('data'))
    assert when_send_get_list_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('messages') is None
    assert result is not None
    assert result[0]['id'] is not None
    assert result[0]['name'] is not None
    assert result[0]['users'] is not None
    assert result[0]['users'][0]['id'] is not None
    assert result[0]['users'][0]['account'] is not None
    assert result[0]['users'][0]['name'] is not None
