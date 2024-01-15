import sqlalchemy
from sqlalchemy.orm import Session as SessionType
from models.models import Session

from models.projects import Project
from models.category_projects import Category

def sess(fun):
    def wrapper(*args, **kwargs):
        session: SessionType = Session()
        fun(session, *args, **kwargs)
        return wrapper



def add_project(name, description,tech_task, square, body, price, img, category):
    session: SessionType = Session()
    category1 = session.query(Category).filter_by(name=category).one_or_none()
    project = Project(name=name, description=description, tech_task=tech_task, square=square, body=body, price=price, img=img, category=category1 )
    session.add(project)

    session.commit()
    session.close()
    return project


def show_project_all():
    session: SessionType = Session()
    projects = session.query(Project).join(Category, Category.id == Project.category_id).all()
    session.close()
    return projects



def del_project(name_project):
    session: SessionType = Session()
    name = session.query(Project).filter_by(name=name_project).one_or_none()
    session.delete(name)
    session.commit()
    session.close()
    return f'запись {name.name} удвлена'

def project_more(name):
    session: SessionType = Session()
    name_pr = session.query(Project).filter_by(name=name).join(Category, Category.id == Project.category_id)
    session.close()
    return name_pr



def get_project(project_id):
    session: SessionType = Session()
    name_pr = session.query(Project).get(project_id)
    session.close()
    return name_pr

def change_project(project_id, newname, newdescription, newtech_task, newsquare, newbody, newprice, newimg, newcategory):
    session: SessionType = Session()
    name_pr = session.query(Project).get(project_id)
    name_pr.name = newname
    name_pr.description = newdescription
    name_pr.tech_task = newtech_task
    name_pr.square = newsquare
    name_pr.body = newbody
    name_pr.price = newprice
    name_pr.img = newimg
    name_pr.category_id = newcategory
    session.commit()
    session.close()
    return name_pr
#


# dd = show_project_all()
#
# for i in dd:
#     print(i.__dict__)



