## 本地运行（不使用 Docker）

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
# 这一步是复制环境变量配置文件模板，生成项目所需的 .env 文件
copy .env.example .env
# 首先运行数据库迁移，确保数据库结构是最新的
alembic upgrade head

# 然后启动开发服务器，--reload 参数可以在代码变动时自动重启应用
uvicorn app.main:app --reload
```

## 登录拿 Token

- POST `/api/auth/token`（表单：`username` / `password`）
- GET `/api/users/me`（Header：`Authorization: Bearer <token>`）

