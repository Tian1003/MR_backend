Feature: 網頁端教師、維運人員登入
    Scenario Outline: 正常登入
        Given account欄位為 <account>, password欄位為 <password>
        When 發送 post 請求至後端 endpoint /api/teacher/login
        Then 返回 status code 200;
            data 欄位包含 id, account, name;
            messages 欄位值為 null;
            status 欄位值為 "success"

        Examples:
            | account   | password  |
            | teacher   | teacher   |
            | developer | developer |
