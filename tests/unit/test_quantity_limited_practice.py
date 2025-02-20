from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/unit/quantity_limited_practice.feature')


@given(
    parsers.parse(
        '姓名:{name}, 題目類型:{type_id_list},查詢的起始時間:{finished_start}, 查詢的結束時間:{finished_end},班級:{class_id_list},頁碼:{page},每頁呈現比數:{per_page}'),
    target_fixture='given_get_quantitly_limited_prectice',
    converters={
        'name': str,
        'type_id_list': int,
        'finished_start': str,
        'finished_end': str,
        'class_id_list': int,
        'page': int,
        'per_page': int,
    }
)
def given_get_quantitly_limited_prectice(name, type_id_list, finished_start, finished_end, class_id_list, page, per_page):
    assert name in ["developer", "Lonee"]
    assert type_id_list in [2, 1]
    assert class_id_list in [1, 5]
    assert page in [1, 1]
    assert per_page in [10, 50]
    return {
        "name": name,
        "type_id_list": type_id_list,
        "finished_start": finished_start,
        "finished_end": finished_end,
        "class_id_list": class_id_list,
        "page": page,
        "per_page": per_page
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
        '發送 get 請求至後端 endpoint /api/quantity_limited_practices?page={page}&per_page={per_page}'),
    target_fixture='when_send_uantitly_limited_prectice_request',
    converters={
        'page': int,
        'per_page': int
    }
)
def when_send_uantitly_limited_prectice_request(client, given_get_quantitly_limited_prectice, page, per_page):
    headers = {
        'Cookie': f'session={get_session_value(client)}'
    }
    response = client.get(f'/api/quantity_limited_practices?page={page}&per_page={per_page}', json=given_get_quantitly_limited_prectice,
                          content_type='application/json', headers=headers)
    return response


@then('返回 status code 200;\ndata 欄位包含;\nmax_page 欄位不可為 null;\nmessages 欄位值為 null;\nstatus 欄位值為 "success";\ntotal 欄位不可為 null;')
def then_check_response(when_send_uantitly_limited_prectice_request):
    json_response = when_send_uantitly_limited_prectice_request.get_json()
    assert when_send_uantitly_limited_prectice_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('max_page') is not None
    assert json_response.get('messages') is None
    assert json_response.get('total') is not None
    data = json_response.get('data')
    if isinstance(data, list):
        for sub_item in data:
            assert sub_item.get('class_') is not None
            assert sub_item.get('class_').get('id') is not None
            assert sub_item.get('class_').get('name') is not None
            assert sub_item.get('finished_at') is not None
            assert sub_item.get('id') is not None
            assert sub_item.get('level1_time') is not None
            assert sub_item.get('level1_total_quantity') is not None
            assert sub_item.get('level2_time') is not None
            assert sub_item.get('level2_total_quantity') is not None
            assert sub_item.get('level3_time') is not None
            assert sub_item.get('level3_total_quantity') is not None
            assert sub_item.get('type') is not None
            assert sub_item.get('type').get('id') is not None
            assert sub_item.get('type').get('name') is not None
            assert sub_item.get('user') is not None
            assert sub_item.get('user').get('id') is not None
            assert sub_item.get('user').get('name') is not None

    else:
        print('no data')
