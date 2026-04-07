from typing import Optional, List
from datetime import datetime

from sqlalchemy import String, Boolean, ForeignKey, func, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy(model_class=declarative_base(), engine_options=dict(echo=True))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    first_name: Mapped[str] = mapped_column(String(255), default=None, nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), default=None, nullable=True)
    password_: Mapped[str] = mapped_column(String(1000))
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    created: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
    posts: Mapped[List["Post"]] = relationship(back_populates="user")

    @property
    def password(self) -> str:
        return self.password_

    @password.setter
    def password(self, raw_password: str) -> None:
        self.password_ = generate_password_hash(raw_password)

    def is_verify_password(self, raw_password) -> bool:
        return check_password_hash(self.password_, raw_password)


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(1000))
    text: Mapped[str] = mapped_column(Text())
    created: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    user: Mapped[User] = relationship(back_populates="posts")
    image: Mapped[str] = mapped_column(String(1000), default=None, nullable=True)
