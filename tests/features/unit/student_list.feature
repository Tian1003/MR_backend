Feature: 網頁端學生表單搜尋
    Scenario Outline: 正常搜尋表單
        Given class_id_list 欄位 <class_id_list>
        When 發送 get 請求至後端 endpoint /api/students
        Then 返回 status code 200;
            data 欄位包含 id, account, name, class_;
                class_ 欄位包含 id, name;
            messages 欄位值為 null;
            status 欄位值為 "success"
            total 欄位值不為 0

        Examples:
            | class_id_list|
            | 1 |
            | 1,2 |
