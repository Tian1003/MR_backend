Feature: 網頁端限題練習列表搜尋
    Scenario Outline: 透過班級篩選限題練習列表
        Given account欄位為 <account>, password欄位為 <password>
        When 前往登入頁面
        And 輸入 account 和 password 後點擊登入按鈕
        And 前往 home 頁面
        And 點擊「學生練習」側欄選項
        And 點擊「限題」標籤選項
        And 點擊「班級」下拉選單
        And 點擊第一個班級選項
        Then 確認限題練習列表僅有此班級學生的限題練習作答記錄
        And 取消點擊第一個班級選項
        And 取消點擊「班級」下拉選單

        Examples:
            | account   | password  |
            | teacher   | teacher   |

    Scenario Outline: 透過姓名篩選限題練習列表
        Given 給予姓名測試值 <name>
        When 在「姓名」輸入框測試值
        Then 確認限題練習列表僅有此姓名學生的限題練習作答記錄
        And 刪除「姓名」輸入框字串

        Examples:
            | name |
            | 張彥廷 |
            | 張靜宜 |

    Scenario Outline: 透過題型篩選限題練習列表
        When 點擊「題型」下拉選單
        And 點擊第一個題型選項
        Then 確認限題練習列表僅有此題型的限題練習作答記錄
        And 取消點擊第一個題型選項
        And 取消點擊「題型」下拉選單

    Scenario Outline: 透過時間區間篩選限題練習列表
        When 點擊「開始日期」下拉選單
        And 選擇2024/03/03的日期
        And 點擊「結束日期」下拉選單
        And 選擇2024/03/05的日期
        Then 確認限題練習列表僅有此時間區間的限題練習作答記錄
        And 點擊列表中第一筆紀錄的姓名欄位
        And 確認圖表包含三個關卡