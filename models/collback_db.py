from sqlalchemy import Column, Boolean, String, Integer, Text


from .models import Base
from .mixins import TimestampMixin


class CollbackDb(TimestampMixin, Base):
    username = Column(String(40), unique=False, nullable=False)
    phonenumber = Column(String(20),  unique=False, nullable=False,)
    short_deskription = Column(String(500),unique=False, nullable=True )
    files = Column(Text, nullable=True)


    def __str__(self):

        return f"Collback(username={self.username!r}, phonenumber={self.phonenumber})"