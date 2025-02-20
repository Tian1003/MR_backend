Feature: 網頁端班級列表
    Scenario Outline: 正常列出班級列表
        When 發送 get 請求至後端 endpoint /api/classes
        Then 返回 status code 200;
            data 欄位包含 id, name, users;
                users 欄位包含 id, account, name;
            messages 欄位值為 null;
            status 欄位值為 "success"
            total 欄位值不為 0
