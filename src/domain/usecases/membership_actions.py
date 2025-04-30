from secrets import token_urlsafe

import inject
import jwt
from flask import current_app
from hashlib import sha256

from src.domain.models import NewUser, User
from src.infra.repositories.postgres.user_repository import UserRepository
from src.infra.repositories.redis.auth_repository import AuthRepository

class AuthUserAction:
    user_repository = inject.attr(UserRepository)

    def execute(self, user_id: str, password: str) -> bool:
        user = self.user_repository.get_user(user_id)
        if user is None:
            return False
        hashed_password = sha256(password.encode("utf-8")).hexdigest()
        return user.password_hash == hashed_password

class CreateAuthTokenAction:
    auth_repository = inject.attr(AuthRepository)

    def execute(self, user_id: str) -> str:
        secret = token_urlsafe(32)
        hashed_secret = sha256(secret.encode("utf-8")).hexdigest()
        payload = {
            "user_id": user_id,
            "secret": secret,
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        self.auth_repository.save_token(hashed_secret, user_id)
        return token

class ValidateAuthTokenAction:
    auth_repository = inject.attr(AuthRepository)

    def execute(self, token: str) -> str | None:
        try:
            payload = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"],
            )
            secret = payload["secret"]
            hashed_secret = sha256(secret.encode("utf-8")).hexdigest()
            user_id = self.auth_repository.get_token(hashed_secret)
            if user_id is None:
                return None
            return user_id.decode("utf-8")
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

class GetUserAction:
    user_repository = inject.attr(UserRepository)

    def execute(self, user_id: str) -> User | None:
        result = self.user_repository.get_user(user_id)
        if result is None:
            return None

        return User(
            id=result.id,
            name=result.name,
            email=result.email,
            username=result.username,
            created_at=result.created_at,
            updated_at=result.updated_at,
        )

class RegisterUserAction:
    user_repository = inject.attr(UserRepository)

    def execute(self, new_user: NewUser) -> None:
        new_user.password_hash = sha256(new_user.password.encode("utf-8")).hexdigest()
        self.user_repository.add_user(new_user)

class UpdateUserPasswordAction:
    user_repository = inject.attr(UserRepository)

    def execute(self, user_id: str, new_password: str) -> None:
        hashed_password = sha256(new_password.encode("utf-8")).hexdigest()
        self.user_repository.update_user_password(user_id, hashed_password)
