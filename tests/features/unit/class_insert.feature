Feature: 網頁端班級新增
    Scenario Outline: 正常新增
        Given name 欄位 <name>
        When 發送 post 請求至後端 endpoint /api/classes
        Then 返回 status code 200;
            data 欄位包含 id, name;
            messages 欄位值為 null;
            status 欄位值為 "success"
            total 欄位值不為 0
        And 刪除剛剛新增的班級資料

        Examples:
            | name |
            | test1 |
            | test2 |
