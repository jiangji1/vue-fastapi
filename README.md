# f1 - FastAPI + Vue 管理后台脚手架（A：router/service/repository）

## 目录

- `backend/`: FastAPI（账号密码登录 + JWT）、SQLAlchemy 2、Alembic、MySQL
- `frontend/`: Vue3 + TypeScript + Element Plus 管理后台骨架

## 本地启动（Docker Compose）

在 `c:\pycode\f1` 下执行：

```bash
docker compose up --build
```

然后：

- 后端 API：`http://localhost:8000`
- 接口文档：`http://localhost:8000/docs`

## 后端环境变量

Compose 已内置默认值。若你要本地裸跑后端，可参考 `backend/.env.example`。

## 初始账号

首次启动后端会在启动时自动创建一个默认管理员账号（见 `backend/app/bootstrap.py`）：

- username: `admin`
- password: `admin123`

建议启动后立刻修改密码。

