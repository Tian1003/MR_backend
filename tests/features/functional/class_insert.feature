Feature: 網頁端新增班級功能
    Scenario Outline: 新增班級
        Given 班級名稱：<name> 
        When 前往登入頁面
        And 輸入 教師的帳號：<account> 和 密碼：<password> 後點擊登入按鈕
        And 前往 home 頁面
        And 點擊「班級管理」側欄選項
        And 點擊「新增班級」按鈕
        And 在「班級」輸入框測試值
        And 點擊「新增」按鈕
        Then 確認班級列表有此新增的班級

        Examples:
            | account | password | name |
            | teacher | teacher | appleClass |
            
            
