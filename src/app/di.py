import inject
import redis
from flask import Flask
from sqlalchemy.orm import scoped_session

from src.domain.usecases.product_actions import GetProductsAction
from src.domain.usecases.membership_actions import GetUserAction
from src.infra.repositories.postgres.db import session
from src.infra.repositories.postgres.product_repository import ProductRepository
from src.infra.repositories.postgres.user_repository import UserRepository
from src.infra.repositories.redis import create_redis_client

def init_app(app: Flask):
    def my_config(binder):
        binder.bind_to_constructor(scoped_session, lambda: session)
        binder.bind_to_constructor(
            redis.Redis, lambda: create_redis_client(app),
        )

        # repositories
        binder.bind(ProductRepository, ProductRepository())
        binder.bind(UserRepository, UserRepository())

        # actions
        binder.bind(GetUserAction, GetUserAction())
        binder.bind(GetProductsAction, GetProductsAction())

    inject.configure(my_config)
