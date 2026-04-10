from __future__ import annotations

# 迁移环境会 import Base.metadata，这里集中导入模型，避免遗漏
from app.db.base import Base  # noqa: F401
from app.models import User  # noqa: F401

