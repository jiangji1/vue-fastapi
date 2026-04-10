from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def get_by_username(self, db: Session, *, username: str) -> User | None:
        return db.scalar(select(User).where(User.username == username))

    def get(self, db: Session, *, user_id: int) -> User | None:
        return db.get(User, user_id)

    def create(self, db: Session, *, username: str, hashed_password: str, is_superuser: bool = False) -> User:
        user = User(username=username, hashed_password=hashed_password, is_superuser=is_superuser, is_active=True)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

