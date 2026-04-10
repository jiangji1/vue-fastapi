from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.repositories.user_repo import UserRepository


class AuthService:
    def __init__(self, user_repo: UserRepository | None = None) -> None:
        self.user_repo = user_repo or UserRepository()

    def authenticate(self, db: Session, *, username: str, password: str) -> str | None:
        user = self.user_repo.get_by_username(db, username=username)
        if not user or not user.is_active:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return create_access_token(subject=str(user.id))

    def ensure_user(self, db: Session, *, username: str, password: str, is_superuser: bool = False):
        user = self.user_repo.get_by_username(db, username=username)
        if user:
            return user
        return self.user_repo.create(
            db,
            username=username,
            hashed_password=hash_password(password),
            is_superuser=is_superuser,
        )

