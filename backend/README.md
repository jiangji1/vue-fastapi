## 本地运行（不使用 Docker）

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

默认使用 SQLite（`backend/.data/app.db`），无需安装 MySQL。
若你切换到 MySQL，才需要运行 `alembic upgrade head` 做迁移。

## 登录拿 Token

- POST `/api/auth/token`（表单：`username` / `password`）
- GET `/api/users/me`（Header：`Authorization: Bearer <token>`）

