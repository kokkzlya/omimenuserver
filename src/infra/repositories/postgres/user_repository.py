import inject
from sqlalchemy import select, or_
from sqlalchemy.orm import scoped_session

from src.domain import models
from src.infra.repositories.postgres.entities import User

class UserRepository:
    session = inject.attr(scoped_session)

    def get_user(self, user_id: str) -> models.User | None:
        query = select(User).where(or_(User.username == user_id, User.email == user_id))
        user = self.session.execute(query).scalars().first()
        if user is None:
            return None
        return models.User.model_validate(user, from_attributes=True)

    def add_user(self, user: models.NewUser) -> None:
        new_user = User(
            name=user.name,
            email=user.email,
            username=user.username,
            password_hash=user.password_hash,
        )
        self.session.add(new_user)
        self.session.commit()

    def update_user_password(self, user_id: str, new_password_hash: str) -> None:
        query = select(User).where(or_(User.username == user_id, User.email == user_id))
        user = self.session.execute(query).scalars().first()
        if user is None:
            return
        user.password_hash = new_password_hash
        self.session.commit()
