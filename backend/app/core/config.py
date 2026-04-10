from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """集中管理配置，便于在容器与 K8s 中注入环境变量。"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "f1-api"
    env: str = "dev"

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
        # PyMySQL 使用 mysql+pymysql
        return (
            f"mysql+pymysql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}?charset=utf8mb4"
        )


settings = Settings()

