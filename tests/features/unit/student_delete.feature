Feature: 網頁端學生資料刪除
    Scenario Outline: 正常刪除
        Given user_id 欄位 <id>
        When 發送 delete 請求至後端 endpoint /api/students/<id>
        Then 返回 status code 200;
            messages 欄位值為 null;
            status 欄位值為 "success"

        Examples:
            | id |
            | 3 |
            | 4 |
