from sqlalchemy.orm import Session as SessionType


from models.models import Session

from models.category_projects import Category
from models.projects import Project

def add_category(name_cat):
    session: SessionType = Session()
    if session.query(Category).filter_by(name=name_cat.strip()).one_or_none():

        return f'категория {name_cat} уже создана'
    else:
        category = Category(name=name_cat.strip())
        session.add(category)
        session.commit()
        session.close()
        return 0

def show_category_all():
    session: SessionType = Session()
    category = session.query(Category).all()

    session.close()
    return category

def del_category(name_cat):
    session: SessionType = Session()
    name = session.query(Category).filter_by(name=name_cat).one_or_none()
    session.delete(name)
    session.commit()
    session.close()
    return 0


def show_category_project(cat_id):
    session: SessionType = Session()
    category_id  = session.query(Category).filter_by(id=cat_id).join(Project, Project.category_id == Category.id)

    session.close()
    return category_id


def show_next_project(pr_name, cat_id):
    category = show_category_project(cat_id)
    for item in category:
        for project in item.project:
            if pr_name == project.name and item.project.index(project) + 1 == len(item.project):
                return item.project[0:1]
            elif pr_name == project.name:
                return item.project[item.project.index(project) + 1: item.project.index(project) + 2]





# dd = show_category_project(5)
#
# for i in dd:
#     for name in i.project:
#         print(name.name)
#         print(name.img.split(' ')[0])
#         print(name.description)

# dd = del_category('test')
# print(dd)
#
# dd1 = show_category_all()
#
# gg = {id1.id: id1.name  for id1 in dd1}
# print(gg[1])
