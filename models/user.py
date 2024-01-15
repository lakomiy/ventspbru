from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import relationship

from .models import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):
    username = Column(String(20), unique=True, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    password = Column(String(30),  nullable=False)

    def __str__(self):
        return f"User(username={self.username!r}, is_staff={self.is_staff})"