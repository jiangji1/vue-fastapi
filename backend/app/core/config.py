from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """集中管理配置，便于在容器与 K8s 中注入环境变量。"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "f1-api"
    env: str = "dev"

    # 数据库：
    # - sqlite（默认）：本地文件数据库，无需安装 MySQL
    # - mysql：若你未来需要再切回 MySQL，可配置 mysql 相关环境变量
    db_scheme: str = "sqlite"  # sqlite | mysql
    sqlite_path: str = "./.data/app.db"

    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str = "f1"
    db_password: str = "f1"
    db_name: str = "f1"

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60

    bootstrap_admin_username: str = "admin"
    bootstrap_admin_password: str = "admin123"

    @property
    def sqlalchemy_database_uri(self) -> str:
        if self.db_scheme.lower() == "sqlite":
            p = Path(self.sqlite_path)
            if not p.is_absolute():
                p = Path.cwd() / p
            p.parent.mkdir(parents=True, exist_ok=True)
            return f"sqlite:///{p.as_posix()}"

        # mysql+pymysql
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}?charset=utf8mb4"


settings = Settings()

