Feature: 網頁端學生資料新增
    Scenario Outline: 正常新增
        Given class_id 欄位 <class_id>, name 欄位 <name>, account 欄位 <account>
        When 發送 post 請求至後端 endpoint /api/students
        Then 返回 status code 200;
            data 欄位包含 id, account, name, class_;
                class_ 欄位包含 id, name;
            messages 欄位值為 null;
            status 欄位值為 "success"
        And 刪除剛剛新增的學生資料

        Examples:
            | class_id | name | account |
            | 1 | test1 | test1 |
            | 2 | test2 | test2 |
