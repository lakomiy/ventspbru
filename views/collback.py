from pathlib import Path
import os
from phonenumbers import NumberParseException

from models.collback_db import CollbackDb
from sqlalchemy.orm import Session as SessionType
from models.models import Session

import phonenumbers


# number = "+79627205448"
# number1 = phonenumbers.parse(number)
# print(type(number))
# print(type(phonenumbers.is_valid_number(number1)))

def callback_db(username: str, phonenumber: str, short_deskription: str, files: str ):
    session: SessionType = Session()
    phonenumber1 = phonenumbers.parse(phonenumber)
    try:
        phonenumbers.is_valid_number(phonenumber1)

        user_callback = CollbackDb(username=username, phonenumber=phonenumber, short_deskription=short_deskription, files=files)
        session.add(user_callback)
        session.commit()
        session.close()
        return user_callback
    except NumberParseException:
        return None


def callback_show():
     session: SessionType = Session()
     callback_all = session.query(CollbackDb).all()

     session.close()
     return callback_all

def download_file_callback(id):
    session: SessionType = Session()
    callback_file = session.query(CollbackDb).filter_by(id=id)
    session.close()
    return callback_file


def del_callback_rowdb(row_id):
    session: SessionType = Session()
    name = session.query(CollbackDb).filter_by(id=row_id).one_or_none()
    session.delete(name)
    session.commit()
    session.close()
    return 0

