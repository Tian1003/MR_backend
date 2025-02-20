# MR_backend

## 版本需求
* Python 3.8.5 (Python ^3)
* MySQL 8

## Step 1 下載依賴
透過 `requirements.txt` 下載依賴

Windows
```shell
pip install -r requirements.txt
```

Mac
```shell
pip3 install -r requirements.txt
```

## Step 2 複製 .env.example 並修改為.env
`.env` 檔案中填入資料庫相關參數

Windows powershell
```powershell
Copy-Item .env.example .env
```

Windows CMD
```cmd
copy .env.example .env
```

Mac
```cmd
cp .env.example .env
```

## Step 3 建立資料庫
執行 `initial_db.py`

Windows
```powershell
python ./initial_db.py
```

Mac
```powershell
python3 ./initial_db.py
```

## Step 4 檢查資料庫
看到八張資料表且部分表有資料，就代表資料庫建立成功了🥳

## Step 5 啟動 Flask 專案
Windows
```
flask run
```

Windows auto-reload
```
flask --app wsgi.py --debug run
```

Mac
```
python3 -m flask run
```

Mac auto-reload
```
python3 -m flask --app wsgi.py --debug run
```

## (Option) 查看專案 API 文件
進入 api_documentation 資料夾
```powershell
cd ./api_documentation/
```

啟動 node server
```powershell
npx serve
```

## (Option) 塞一點假資料 已整合至Step 3

Windows
```powershell
flask seed run --root .\app\seeds
```

Mac
```powershell
python3 -m flask seed run --root .\app\seeds
```

## (Option) 來玩一下測試
執行前需先確認相依都已安裝

Windows
```powershell
pytest -W ignore::pytest.PytestDeprecationWarning
```
