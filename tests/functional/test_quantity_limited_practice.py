import time
from datetime import datetime
from pytest_bdd import scenario, given, when, then, parsers
from functools import partial
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

scenario = partial(scenario, "../features/functional/quantity_limited_practice.feature")
selected_class = ""
selected_question_type = ""
selected_start_date = ""
selected_end_date = ""

@scenario("透過班級篩選限題練習列表")
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

@when("前往 home 頁面")
def check_url(driver, prefix):
    WebDriverWait(driver, 5).until(
        EC.url_contains(f"{prefix}/home")
    )
    assert driver.current_url == f"{prefix}/home"

@when("點擊「學生練習」側欄選項")
def when_click_student_practice(driver):
    student_practice_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]')))
    student_practice_tab.click()

@when("點擊「限題」標籤選項")
def when_click_quantity_limited(driver):
    quantity_limited_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]')))
    quantity_limited_tab.click()

@when("點擊「班級」下拉選單")
def when_click_class_drop_down(driver):
    class_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div[1]')))
    class_drop_down.click()

@when("點擊第一個班級選項")
def when_click_first_class(driver):
    global selected_class

    first_class = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div[2]/div[1]/label')))
    first_class.click()

    selected_class = first_class.text
    assert selected_class != ""

@then('確認限題練習列表僅有此班級學生的限題練習作答記錄')
def then_check_table_result(driver):
    global selected_class
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        assert row.find_element(By.XPATH, 'td[2]').text == selected_class

@then('取消點擊第一個班級選項')
def when_click_first_class(driver):
    first_class = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div[2]/div[1]/label')))
    first_class.click()

@then('取消點擊「班級」下拉選單')
def when_click_class_drop_down(driver):
    class_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[1]/div/div[1]')))
    class_drop_down.click()


@scenario("透過姓名篩選限題練習列表")
def test_filter_by_name():
    pass

@given(
    parsers.parse('給予姓名測試值 {name}'),
    target_fixture='given_valid_name',
    converters={
        'name': str
    }
)
def given_valid_name(name):
    assert name in ["張彥廷", "張靜宜"]
    return name

@when('在「姓名」輸入框測試值')
def when_key_in_name(driver, given_valid_name):
    input_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, 'first_name')))
    input_name.clear()
    for n in given_valid_name:
        input_name.send_keys(n)
        time.sleep(0.1)

@then('確認限題練習列表僅有此姓名學生的限題練習作答記錄', target_fixture='then_check_table_result')
def then_check_table_result(driver, given_valid_name):
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        assert row.find_element(By.XPATH, 'td[3]').text == given_valid_name

@then('刪除「姓名」輸入框字串')
def then_check_table_result(driver):
    input_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, 'first_name')))
    input_name.clear()


@scenario("透過題型篩選限題練習列表")
def test_filter_by_question_type():
    pass

@when("點擊「題型」下拉選單")
def when_click_question_type_drop_down(driver):
    question_type_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[3]/div/div[1]')))
    question_type_drop_down.click()

@when("點擊第一個題型選項")
def when_click_first_type(driver):
    global selected_question_type

    first_type = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[3]/div/div[2]/div[1]/label')))
    first_type.click()

    selected_question_type = first_type.text
    assert selected_question_type != ""

@then('確認限題練習列表僅有此題型的限題練習作答記錄')
def then_check_table_result(driver):
    global selected_question_type
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        assert row.find_element(By.XPATH, 'td[4]').text == selected_question_type

@then('取消點擊第一個題型選項')
def when_click_first_type(driver):
    first_type = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[3]/div/div[2]/div[1]/label')))
    first_type.click()

@then('取消點擊「題型」下拉選單')
def when_click_question_type_drop_down(driver):
    question_type_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[3]/div/div[1]')))
    question_type_drop_down.click()


@scenario("透過時間區間篩選限題練習列表")
def test_filter_by_date():
    pass

@when("點擊「開始日期」下拉選單")
def when_click_start_date_drop_down(driver):
    date_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div[1]/div/input')))
    date_drop_down.click()

@when("選擇2024/03/03的日期")
def when_click_start_date(driver):
    global selected_start_date

    start_date = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]')))
    start_date.click()

    date = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div[1]/div/input')))

    selected_start_date = date.get_attribute("value")
    assert selected_start_date == "2024/03/03"

@when("點擊「結束日期」下拉選單")
def when_click_date_drop_down(driver):
    date_drop_down = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div[2]/div/input')))
    date_drop_down.click()

@when("選擇2024/03/05的日期")
def when_click_end_date(driver):
    global selected_end_date

    end_date = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]')))
    end_date.click()

    date = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div[2]/div/input')))

    selected_end_date = date.get_attribute("value")
    assert selected_end_date == "2024/03/05"

@then('確認限題練習列表僅有此時間區間的限題練習作答記錄')
def then_check_table_result(driver):
    global selected_start_date, selected_end_date
    start_datetime = datetime.strptime(f'{selected_start_date} 00:00', "%Y/%m/%d %H:%M")
    end_datetime = datetime.strptime(f'{selected_end_date} 23:59', "%Y/%m/%d %H:%M")
    time.sleep(1)

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        row_datetime = datetime.strptime(row.find_element(By.XPATH, 'td[11]').text, "%Y/%m/%d %H:%M")
        assert row_datetime >= start_datetime and row_datetime <= end_datetime

@then("點擊列表中第一筆紀錄的姓名欄位")
def then_click_first_data(driver):
    first_data = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[3]')))
    first_data.click()

@then("確認圖表包含三個關卡")
def then_check_chart(driver):
    first_chart= WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[1]/p')))
    assert first_chart.text == "第一關"

    second_chart= WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/p')))
    assert second_chart.text == "第二關"

    third_chart= WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/p')))
    assert third_chart.text == "第三關"