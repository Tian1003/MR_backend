import os
from sqlalchemy import create_engine

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_USER = os.getenv('DB_ACCOUNT', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'hapopo1003')
SCHEMA_NAME = os.getenv('SCHEMA_NAME', 'Testing')

# 測試 SQLAlchemy 連線
try:
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{SCHEMA_NAME}")
    with engine.connect() as conn:
        print("✅ MySQL 連線成功！")
except Exception as e:
    print("❌ MySQL 連線失敗，錯誤訊息：", e)
