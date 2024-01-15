from sqlalchemy import Column, Boolean, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .models import Base
from .mixins import TimestampMixin


class Category(TimestampMixin, Base):
    name = Column(
        String(300),
        nullable=False,
        default="",
        server_default="",

    )

    project = relationship(
        "Project",
        back_populates="category",

    )
    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r})"
        )