import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios('../features/functional/class_insert.feature')

@given(
    parsers.parse('班級名稱：{name}'),
    target_fixture='given_valid_parameters'
)
def given_valid_parameters(name):
    assert name in ["appleClass"]
    return{
        "name" : name
    }

@when("前往登入頁面", target_fixture='get_login_page')
def get_login_page(driver, prefix):
    driver.get(f"{prefix}")

@when(
    parsers.parse('輸入 教師的帳號：{account} 和 密碼：{password} 後點擊登入按鈕'),
    target_fixture='type_account_and_password',
)
def type_account_and_password(driver,account,password):
    account_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, "account")))
    password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, "password")))

    account_input.send_keys(account)
    password_input.send_keys(password)

    login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME,"bg-loginbtn")))
    login_btn.click()

@when('前往 home 頁面')
def check_url(driver, prefix):
    WebDriverWait(driver, 5).until(
        EC.url_contains(f"{prefix}/home")
    )
    assert driver.current_url == f"{prefix}/home"

@when('點擊「班級管理」側欄選項')
def when_click_student_tap(driver):
    class_menager_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="side"]/div/div/ul/li[4]')))
    class_menager_tab.click()

@when('點擊「新增班級」按鈕')
def when_click_insert_class_button(driver):
    insert_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'insert')))
    insert_button.click()

@when(parsers.parse('在「班級」輸入框測試值'))
def when_input_class_name(driver,given_valid_parameters):
    name_input = WebDriverWait(driver,5).until(EC.presence_of_element_located(
        (By.ID,"name")
    ))
    name_input.send_keys(given_valid_parameters.get("name"))

@when('點擊「新增」按鈕')
def when_click_conform_button(driver):
    conform_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div/div/form/div[2]/button[2]')))
    conform_button.click()

@then('確認班級列表有此新增的班級')
def check_added(driver,given_valid_parameters):
    time.sleep(1)
    is_exist = False
    class_name = given_valid_parameters.get("name")

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        if row.find_element(By.XPATH, 'td[2]').text == class_name:
            is_exist = True
            break

    assert is_exist == True