from __future__ import annotations

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.db.session import SessionLocal
from app.bootstrap import bootstrap


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)
    app.include_router(api_router)
    return app


app = create_app()


@app.on_event("startup")
def _on_startup() -> None:
    # 这里不自动建表：生产更推荐走 Alembic 迁移；本地可先跑一次迁移再启动
    with SessionLocal() as db:
        bootstrap(db)

