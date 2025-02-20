import time
from pytest_bdd import scenario, given, when, then, parsers
from functools import partial
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


scenario = partial(scenario, "../features/functional/student_list.feature")
selected_class = ""


@scenario("透過班級篩選學生")
def test_filter_by_class():
    pass


@given(
    parsers.parse('account欄位為 {account}, password欄位為 {password}'),
    target_fixture='given_valid_account_password',
    converters={
        'account': str
    }
)
def given_valid_account_password(account, password):
    assert account in ["teacher"]
    assert password in ["teacher"]

    return {
        "account": account,
        "password": password
    }


@when("前往登入頁面", target_fixture='get_login_page')
def get_login_page(driver, prefix):
    driver.get(f"{prefix}")


@when("輸入 account 和 password 後點擊登入按鈕", target_fixture='get_login_page')
def type_account_and_password(driver, given_valid_account_password):
    account_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, "account")))
    password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, "password")))

    account_input.send_keys(given_valid_account_password.get("account"))
    password_input.send_keys(given_valid_account_password.get("password"))

    login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div/div/div[1]/div/form/button")))
    login_btn.click()


@when('前往 home 頁面')
def check_url(driver, prefix):
    WebDriverWait(driver, 5).until(
        EC.url_contains(f"{prefix}/home")
    )
    assert driver.current_url == f"{prefix}/home"


@when('點擊「學生帳號」側欄選項')
def when_click_class_drop_down(driver):
    student_account_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="side"]/div/div/ul/li[3]')))
    student_account_tab.click()


@when('點擊「班級」下拉選單')
def when_click_class_drop_down(driver):
    class_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div')))
    class_drop_down.click()


@when('點擊第一個選項')
def when_click_first_class(driver):
    global selected_class

    first_class = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div[2]/div[1]/label')))
    first_class.click()

    selected_class = first_class.text
    assert selected_class != ""


@then('確認學生列表僅有此班級學生')
def then_check_table_result(driver):
    global selected_class
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        assert row.find_element(By.XPATH, 'td[2]').text == selected_class


@then('取消點擊第一個選項')
def when_click_first_class(driver):
    first_class = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div[2]/div[1]/label')))
    first_class.click()


@scenario("透過姓名篩選學生")
def test_filter_by_name():
    pass


@given(
    parsers.parse('給予姓名測試值 {name}'),
    target_fixture='given_valid_name',
    converters={
        'account': str
    }
)
def given_valid_name(name):
    assert name in ["test5", "test6"]
    return name


@when('在「姓名」輸入框測試值')
def when_key_in_name(driver, given_valid_name):
    input_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, 'first_name')))
    input_name.clear()
    for n in given_valid_name:
        input_name.send_keys(n)
        time.sleep(0.1)


@then('確認學生列表僅有此姓名學生', target_fixture='then_check_table_result')
def then_check_table_result(driver, given_valid_name):
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        assert row.find_element(By.XPATH, 'td[3]').text == given_valid_name


@then('刪除「姓名」輸入框字串')
def then_check_table_result(driver):
    input_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, 'first_name')))
    input_name.clear()


@scenario("透過帳號篩選學生")
def test_filter_by_account():
    pass


@given(
    parsers.parse('給予帳號測試值 {account}'),
    target_fixture='given_valid_account',
    converters={
        'account': str
    }
)
def given_valid_account(account):
    assert account in ["test5", "test6"]
    return account


@when('在「帳號」輸入框測試值')
def when_key_in_account(driver, given_valid_account):
    input_account = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, 'account')))
    input_account.clear()
    for n in given_valid_account:
        input_account.send_keys(n)
        time.sleep(0.1)


@then('確認學生列表僅有此帳號學生')
def then_check_table_result(driver, given_valid_account):
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        assert row.find_element(By.XPATH, 'td[4]').text == given_valid_account


@then('刪除「帳號」輸入框字串')
def then_check_table_result(driver):
    input_account = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, 'account')))
    input_account.clear()
