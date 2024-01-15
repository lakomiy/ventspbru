from models.user import User

from sqlalchemy.orm import Session as SessionType
from models.models import Session
def get_user(username):
    session: SessionType = Session()
    user = session.query(User).filter_by(username=username).one_or_none()
    session.close()
    return user


# dd = get_user('admin2')
# print(dd)