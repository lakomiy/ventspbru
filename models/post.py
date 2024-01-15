
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .models import Base
from .mixins import TimestampMixin


class Post(TimestampMixin, Base):
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )



    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(title={self.title!r})"
        )