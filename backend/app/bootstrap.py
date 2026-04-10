from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.config import settings
from app.services.auth_service import AuthService


def bootstrap(db: Session) -> None:
    """启动时补齐最小可用数据（默认管理员）。"""

    AuthService().ensure_user(
        db,
        username=settings.bootstrap_admin_username,
        password=settings.bootstrap_admin_password,
        is_superuser=True,
    )

