HoaProject2 - Car Rental API (Contracts CRUD)

Yêu cầu
- Python 3.11+
- PostgreSQL đang chạy và có DB: `HoaDB5`

Cấu hình
1) Tạo file `.env` tại thư mục gốc, điền:
```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/HoaDB5
```

2) Cài đặt dependencies:
```
pip install -r requirements.txt
```

Chạy server
```
uvicorn app.main:app --reload
```

API chính
- GET `/contracts`
- POST `/contracts`
- GET `/contracts/{id}`
- PUT `/contracts/{id}`
- DELETE `/contracts/{id}`

Ghi chú
- ORM không tự `create_all`. Hãy tạo bảng theo DDL Postgres đã cung cấp trước khi chạy.

