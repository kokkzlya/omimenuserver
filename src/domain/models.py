from datetime import datetime

import pydantic
from flask_login import UserMixin

class Product(pydantic.BaseModel):
    id: str | None = None
    name: str
    price: int
    description: str
    category: str
    stock: int = 0
    created_at: datetime | None = None
    updated_at: datetime | None = None

class NewUser(pydantic.BaseModel):
    name: str
    email: str
    username: str
    password: str
    password_hash: str | None

class User(pydantic.BaseModel, UserMixin):
    id: str
    name: str
    email: str
    username: str
    password_hash: str | None = None
    created_at: datetime
    updated_at: datetime

    def get_id(self):
        return id
