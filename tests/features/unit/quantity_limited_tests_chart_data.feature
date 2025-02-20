Feature: 測驗限題圖表
    Scenario Outline: 取得正確圖表資料
        Given 查詢的起始時間: <finished_start>, 查詢的結束時間: <finished_end>
        When 發送 get 請求至後端 endpoint /api/quantity_limited_tests/chart/users/<id>
        Then 返回 status code 200;
            data 欄位包含;
            messages 欄位值為 null;
            status 欄位值為 "success";
            total 欄位不可為 null;
        Examples:
            |finished_start|finished_end|id|
            |2024-03-23|2024-03-30|1|
            |2024-03-25|2024-03-30|2|