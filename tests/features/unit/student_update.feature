Feature: 網頁端學生資料更新
    Scenario Outline: 正常更新
        Given class_id 欄位 <class_id>, name 欄位 <name>, account 欄位 <account>
        When 發送 update 請求至後端 endpoint /api/students/<id>
        Then 返回 status code 200;
            data 欄位包含 id, account, name, class_;
            class_ 欄位包含 id, name;
            messages 欄位值為 null;
            status 欄位值為 "success"

        Examples:
            | id | class_id | name | account |
            | 5 | 5 | test5 | test5 |
