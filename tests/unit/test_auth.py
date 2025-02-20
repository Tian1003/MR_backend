from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/unit/auth.feature')


@given(
    parsers.parse('account欄位為 {account}, password欄位為 {password}'),
    target_fixture='given_valid_account_password',
    converters={
        'account': str
    }
)
def given_valid_account_password(account, password):
    assert account in ["teacher", "developer"]
    assert password in ["teacher", "developer"]

    return {
        "account": account,
        "password": password
    }


@when("發送 post 請求至後端 endpoint /api/teacher/login", target_fixture='when_send_login_request')
def when_send_login_request(client, given_valid_account_password):
    response = client.post('/api/teacher/login', json=given_valid_account_password,
                           content_type='application/json')
    return response


@then('返回 status code 200;\ndata 欄位包含 id, account, name;\nmessages 欄位值為 null;\nstatus 欄位值為 "success"')
def then_check_response(when_send_login_request):
    json_response = when_send_login_request.get_json()
    assert when_send_login_request.status_code == 200
    assert json_response.get('status') == 'success'
    assert json_response.get('messages') is None
    assert json_response.get('data').get('id') is not None
    assert json_response.get('data').get('account') is not None
    assert json_response.get('data').get('name') is not None
