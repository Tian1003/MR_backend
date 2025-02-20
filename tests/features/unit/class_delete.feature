Feature: 網頁端班級刪除
    Scenario Outline: 正常刪除
        Given class_id 欄位 <id>
        When 發送 delete 請求至後端 endpoint /api/classes/<id>
        Then 返回 status code 200;
            messages 欄位值為 null;
            status 欄位值為 "success"
            total 欄位值不為 0

        Examples:
            | id |
            | 6  |
