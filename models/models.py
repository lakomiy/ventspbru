from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
    declarative_base,
    declared_attr,
)

from .config import DB_URL, DB_ECHO


class Base:
    @declared_attr
    def __tablename__(cls):


       """"
       название поля в базе

       """

       return f"prvent_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=DB_URL, echo=DB_ECHO)

Base = declarative_base(cls=Base, bind=engine)

session_factory = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Session = scoped_session(session_factory)