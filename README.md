# f1 - FastAPI + Vue 管理后台脚手架（A：router/service/repository）

## 目录

- `backend/`: FastAPI（账号密码登录 + JWT）、SQLAlchemy 2、Alembic、MySQL
- `frontend/`: Vue3 + TypeScript + Element Plus 管理后台骨架

## 本地启动（不使用 Docker / MySQL）

后端默认使用 SQLite（本地文件 `backend/.data/app.db`）。

后端启动：

```bash
cd backend
.\.v\Scripts\activate
uvicorn app.main:app --reload
```

前端启动：

```bash
cd frontend
npm install
npm run dev
```

## 后端环境变量

当前后端默认使用 SQLite（本地文件数据库），无需 Docker/MySQL。若你要本地裸跑后端，可参考 `backend/.env.example`。

## 初始账号

首次启动后端会在启动时自动创建一个默认管理员账号（见 `backend/app/bootstrap.py`）：

- username: `admin`
- password: `admin123`

建议启动后立刻修改密码。

