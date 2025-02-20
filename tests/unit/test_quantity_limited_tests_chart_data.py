from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/unit/quantity_limited_tests_chart_data.feature')


@given(
    parsers.parse('查詢的起始時間: {finished_start}, 查詢的結束時間: {finished_end}'),
    target_fixture='given_valid_parameters',
    converters={
        'finished_start': str,
        'finished_end': str,
    }
)
def given_valid_parameters(finished_start, finished_end):
    return {
        "finished_start": finished_start,
        "finished_end": finished_end,
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
    parsers.parse(
        '發送 get 請求至後端 endpoint /api/quantity_limited_tests/chart/users/{id}'),
    target_fixture='when_send_get_data_request',
    converters={
        'id': int
    }
)
def when_send_get_data_request(client, given_valid_parameters, id):
    headers = {
        'Cookie': f'session={get_session_value(client)}'
    }
    response = client.get(f'/api/quantity_limited_tests/chart/users/{id}', json=given_valid_parameters,
                          content_type='application/json', headers=headers)
    return response


@then('返回 status code 200;\ndata 欄位包含;\nmessages 欄位值為 null;\nstatus 欄位值為 "success";\ntotal 欄位不可為 null;')
def then_check_response(when_send_get_data_request):
    json_response = when_send_get_data_request.get_json()
    assert when_send_get_data_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('messages') is None
    assert json_response.get('total') is not None
    data = json_response.get('data')
    assert len(data["level1_correct_quantity_list"]) == 5
    assert len(data["level1_finished_at_list"]) == 5
    assert len(data["level1_incorrect_quantity_list"]) == 5
    assert len(data["level1_time_list"]) == 5
    assert len(data["level2_correct_quantity_list"]) == 5
    assert len(data["level2_finished_at_list"]) == 5
    assert len(data["level2_incorrect_quantity_list"]) == 5
    assert len(data["level2_time_list"]) == 5
    assert len(data["level3_correct_quantity_list"]) == 5
    assert len(data["level3_finished_at_list"]) == 5
    assert len(data["level3_incorrect_quantity_list"]) == 5
    assert len(data["level3_time_list"]) == 5
