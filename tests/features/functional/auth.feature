Feature: 網頁端教師、維運人員登入
    Scenario Outline: 正常登入
        Given account欄位為 <account>, password欄位為 <password>
        When 前往登入頁面
        And 輸入 account 和 password 後點擊登入按鈕
        Then 前往 home 頁面

        Examples:
            | account   | password  |
            | teacher   | teacher   |
