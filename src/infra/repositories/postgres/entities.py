from datetime import UTC, datetime

import shortuuid
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base

class Product(Base):
    __tablename__ = "product"

    id: Mapped[str] = mapped_column(
        String(32),
        primary_key=True,
        default=shortuuid.uuid,
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(tz=UTC),
        nullable=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(tz=UTC),
        nullable=True,
    )

class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, default=shortuuid.uuid)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(tz=UTC),
        nullable=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(tz=UTC),
        nullable=True,
    )
