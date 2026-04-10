from __future__ import annotations

import logging

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from app.api.router import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.db.session import SessionLocal
from app.bootstrap import bootstrap

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)
    app.include_router(api_router)
    return app


app = create_app()


@app.on_event("startup")
def _on_startup() -> None:
    # 默认 SQLite：本地快速启动，自动建表；生产建议改为 Alembic 迁移流程。
    if settings.db_scheme.lower() == "sqlite":
        Base.metadata.create_all(bind=engine)

    try:
        with SessionLocal() as db:
            bootstrap(db)
    except OperationalError:
        # 非 SQLite 时（例如误配成 mysql），连不上 DB 仍允许应用启动（/docs 可用）。
        logger.warning("DB 连接失败，已跳过启动初始化（bootstrap）。请确认数据库可用后再重试。")

