Feature: 網頁端學生刪除功能
    Scenario Outline: 刪除學生
        Given teacher_account欄位為 <teacher_account>, password欄位為 <password>, target_account欄位為 <target_account>
        When 前往登入頁面
        And 輸入 teacher_account 和 password 後點擊登入按鈕
        And 前往 home 頁面
        And 點擊「學生帳號」側欄選項
        And 點擊 row data 帳號為測試值的刪除按鈕
        And 點擊「刪除」按鈕
        Then 確認學生列表不存在已被刪除的學生

        Examples:
            | teacher_account | password | target_account |
            | teacher | teacher | ejtest |
            
            
