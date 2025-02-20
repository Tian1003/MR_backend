Feature: 測驗限時表單
    Scenario Outline: 取得正確測驗限時表單資料
        Given 姓名:<name>, 題目類型:<type_id_list>,查詢的起始時間:<finished_start>, 查詢的結束時間:<finished_end>,班級:<class_id_list>,頁碼:<page>,每頁呈現比數:<per_page>
        When 發送 get 請求至後端 endpoint /api/time_limited_test?page=<page>&per_page=<per_page>
        Then 返回 status code 200;
            current_page 欄位不可為null;
            data 欄位;
            from 欄位不可為null;
            max_page 欄位不可為 null;
            per_page 欄位不可為null;
            messages 欄位值為 null;
            status 欄位值為 "success";
            to 欄位不可為null;
            total 欄位不可為 null;
        Examples:
            | name   | type_id_list |finished_start|finished_end| class_id_list|page|per_page|
            | developer | 2 |2024-03-23|202403-30|1|1|10|
            | Lonee | 1 |2024-03-25|2024-03-30|5|1|50|