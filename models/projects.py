from sqlalchemy import Column, Boolean, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from .models import Base
from .mixins import TimestampMixin

class Project(TimestampMixin, Base):
    name = Column(
        String(300),
        nullable=False,
        default="",
        server_default="",
        name='заголовок'
    )
    description = Column(
        String(1000),
        nullable=False,
        default="",
        server_default="",
        name='описание'
    )
    tech_task = Column(
        String(1000),
        nullable=False,
        default="",
        server_default="",
        name='Техническое задание'
    )
    square = Column(
        String(300),
        nullable=False,
        default="",
        server_default="",
        name='площадь'

    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
        name='контент'
    )
    price = Column(
        String(300),
        nullable=False,
        default="",
        server_default="",
        name='цена'

    )
    img = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
        name='фото'

    )
    category_id = Column(
        Integer,
        ForeignKey("prvent_categorys.id"),
    )

    category = relationship(
        'Category',
        back_populates="project",
    )
    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r})"
        )