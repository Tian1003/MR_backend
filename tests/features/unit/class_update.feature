Feature: 網頁端班級更新
    Scenario Outline: 正常更新
        Given name 欄位 <name>
        When 發送 update 請求至後端 endpoint /api/classes/<id>
        Then 返回 status code 200;
            data 欄位包含 id, name;
            messages 欄位值為 null;
            status 欄位值為 "success"
            total 欄位值不為 0

        Examples:
            | id | name |
            | 1 | className1 |
            | 2 | className2 |
