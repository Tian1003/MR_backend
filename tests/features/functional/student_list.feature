Feature: 網頁端學生表單搜尋
    Scenario Outline: 透過班級篩選學生
        Given account欄位為 <account>, password欄位為 <password>
        When 前往登入頁面
        And 輸入 account 和 password 後點擊登入按鈕
        And 前往 home 頁面
        And 點擊「學生帳號」側欄選項
        And 點擊「班級」下拉選單
        And 點擊第一個選項
        Then 確認學生列表僅有此班級學生
        And 取消點擊第一個選項

        Examples:
            | account   | password  |
            | teacher   | teacher   |

    Scenario Outline: 透過姓名篩選學生
        Given 給予姓名測試值 <name>
        When 在「姓名」輸入框測試值
        Then 確認學生列表僅有此姓名學生
        And 刪除「姓名」輸入框字串

        Examples:
            | name |
            | test5 |
            | test6 |

    Scenario Outline: 透過帳號篩選學生
        Given 給予帳號測試值 <account>
        When 在「帳號」輸入框測試值
        Then 確認學生列表僅有此帳號學生
        And 刪除「帳號」輸入框字串

        Examples:
            | account |
            | test5 |
            | test6 |

