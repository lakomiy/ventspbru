from dataclasses import dataclass
from typing import List, Any
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi import FastAPI, Request, Form, UploadFile, status, Depends, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi_login import LoginManager

from views.collback import callback_db, callback_show, download_file_callback, del_callback_rowdb
from views.myjobs import add_project, show_project_all, del_project, project_more, get_project, change_project
from views.uploadfile import upload_file
from models.projects import Project
from models.category_projects import Category
from views.category import add_category,  show_category_all, del_category, show_category_project, show_next_project
from views.user import get_user

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/files_collback", StaticFiles(directory="files_collback"), name="files_collback")

templates = Jinja2Templates(directory="templates")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET = "92c1f8908a105379dafbdaa6a653579cb35b2f9d037d2739"
# To obtain a suitable secret key you can run | import os; print(os.urandom(24).hex())

manager = LoginManager(SECRET,"/login",use_cookie=True)
manager.cookie_name = "6a653579cb35b2f9d037d2739"




@app.get("/", response_class=HTMLResponse)
def home(request: Request, message: str = None):
    works = show_project_all()

    return templates.TemplateResponse('index.html', {"request": request, "works": works, 'message':message})


@app.post("/collback" )
def collback( request: Request, files: List[UploadFile], username: str = Form(None), phonenumber : str = Form(None), short_deskription: str = Form(None)):

    if phonenumber == None or username == None:
        message = 'Для обратоной связи укажите, пожалуйста, Ваше имя и номер телефона. В поле краткое описание можно указать email или удобное время для связи. Спасибо'
        return RedirectResponse(f'/error_callback/{message}', status_code=302)
    if files[0].filename:
        name = username + '_' + phonenumber
        list_files = ' '.join(upload_file('files_collback', files,  name))
    else:
        list_files = ''
    callback_db(username=username, phonenumber=phonenumber, short_deskription=short_deskription, files=list_files)
    message = f"Уважаемый {username}, спасибо за проявленный интерес к нашей компании, мы свяжемся с Вами в ближайшее время"
    return RedirectResponse(f'/error_callback/{message}', status_code=302)

@app.get("/privacy", response_class=HTMLResponse)
def privacy(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

#Project
###################################################################################################
@app.get('/projectpage')
def projectpage(request: Request, user = Depends(manager)):
    projects = show_project_all()
    categorys = show_category_all()
    return templates.TemplateResponse('admin/projects.html', {"request": request,'categorys':categorys, 'projects': projects })


@app.post("/projects", response_class= RedirectResponse, status_code=302)
def projects(img: List[UploadFile],
             name: str = Form(), description: str = Form(),
             tech_task: str = Form(), square: str = Form(),
             body: str = Form(), price: str = Form(), category: str = Form(), user = Depends(manager)):

    list_files = upload_file('static/img',img, name)
    add_project(name=name, description=description,tech_task=tech_task,
                          square=square, body=body, price=price, img=' '.join(list_files), category=category)
    return '/projectpage'



@app.post('/delproject/{name_project}', response_class= RedirectResponse, status_code=302)
def delproject(name_project: str, user = Depends(manager)):
    del_project(name_project=name_project)
    return '/projectpage'


@app.get('/changeproject/{id_project}' )
def changeproject(request: Request, id_project: int, user = Depends(manager)):
    project = get_project(id_project)
    categorys = show_category_all()
    return templates.TemplateResponse('admin/changeproject.html', {"request": request, 'categorys': categorys, 'project': project})

@app.post("/changeproject/{id_project}", response_class= RedirectResponse, status_code=302)
def changeproject(img: List[UploadFile], id_project: int,
             name: str = Form(), description: str = Form(),
             tech_task: str = Form(), square: str = Form(),
             body: str = Form(), price: str = Form(), category: str = Form(), change_img: list = Form(), user = Depends(manager)):
    if img[0].filename:    
        list_files = ' '.join(change_img + upload_file('static/img',img, name))
    else:
        list_files = ' '.join(change_img)

    change_project(project_id=id_project ,newname=name, newdescription=description,newtech_task=tech_task,
                          newsquare=square, newbody=body, newprice=price, newimg=list_files, newcategory=category )
    return '/admin'




################################################################################################
@app.get('/error_callback/{message}',  response_class=HTMLResponse)
def error_callback(request: Request, message: str = None):
    return templates.TemplateResponse('error/error_callback.html', {"request": request, "message": message})

@app.get('/categorypage', response_class=HTMLResponse)
def categorypage(request: Request, error=  None, user = Depends(manager)):
    categorys = show_category_all()
    return templates.TemplateResponse('admin/category.html', {"request": request, 'categorys': categorys, 'error':error})

@app.post('/category',  response_class= RedirectResponse, status_code=302)
def category(request: Request, name: str = Form(), user = Depends(manager)):
    cat = add_category(name)
    if cat == 0:
        return '/categorypage'
    else:
        return categorypage(request, error=cat)
@app.post('/delcategory/{name}', response_class= RedirectResponse, status_code=302)
def delcategory(name: str, user = Depends(manager) ):
    del_category(name)
    return '/categorypage'

################################################################################################



##SERVICE#####
@app.get("/conditioning", response_class=HTMLResponse)
def conditioning(request: Request):
    return templates.TemplateResponse('uslugi/conditioning.html', {"request": request})

@app.get("/engineering", response_class=HTMLResponse)
def conditioning(request: Request):
    return templates.TemplateResponse('uslugi/engineering.html', {"request": request})

@app.get("/equipment", response_class=HTMLResponse)
def equipment(request: Request):
    return templates.TemplateResponse('uslugi/equipment.html', {"request": request})

@app.get("/service_teh", response_class=HTMLResponse)
def service_teh(request: Request):
    return templates.TemplateResponse('uslugi/service_teh.html', {"request": request})

@app.get("/mounting", response_class=HTMLResponse)
def mounting(request: Request):
    return templates.TemplateResponse('uslugi/mounting.html', {"request": request})

@app.get("/ventilation", response_class=HTMLResponse)
def ventilation(request: Request):
    return templates.TemplateResponse('uslugi/ventilation.html', {"request": request})

@app.get("/contacts", response_class=HTMLResponse)
def contacts(request: Request):
    return templates.TemplateResponse('contacts/contacts.html', {"request": request})

@app.get("/hol_cam", response_class=HTMLResponse)
def contacts(request: Request):
    return templates.TemplateResponse('uslugi/hol_cam.html', {"request": request})
##END SERVICE#####

###WORKS##########
@app.get("/works_all", response_class=HTMLResponse)
def works_all(request: Request):
    works = show_category_all()
    projects = show_project_all()
    return templates.TemplateResponse('works/works_all.html', {"request": request, "works": works, 'projects': projects})


@app.get("/more/{name}", response_class=HTMLResponse)
def more(request: Request, name : str):
    project = project_more(name)
    return templates.TemplateResponse('works/more.html', {"request": request, 'project': project})

@app.get('/show_next_project/{pr_name}/{cat_id}', response_class= RedirectResponse, status_code=302)
def show_next_pr(pr_name, cat_id):
    project = show_next_project(pr_name=pr_name, cat_id=cat_id)
    return f'/more/{project[0].name}'


@app.post("/more/{name}", response_class=HTMLResponse)
def more(request: Request, name : str,  files: List[UploadFile] = None, username: str = Form(None), phonenumber : str = Form(None), short_deskription: str = Form(None)):
    if username and phonenumber:
        collback(request, files=files, username = username, phonenumber= phonenumber, short_deskription= short_deskription)
    else:
        message = 'Для обратоной связи укажите, пожалуйста, Ваше имя и номер телефона. В поле краткое описание можно указать email или удобное время для связи. Спасибо'
        return templates.TemplateResponse('error/error_callback.html', {"request": request, "message": message})
    message = f"Уважаемый {username}, спасибо за проявленный интерес к нашей компании, мы свяжемся с Вами в ближайшее время"
    return templates.TemplateResponse('error/error_callback.html', {"request": request, "message": message})


@app.get("/category_sort/{id}", response_class=HTMLResponse)
def works_all(request: Request, id : int ):
    works = show_category_all()
    projects = show_category_project(id)
    return templates.TemplateResponse('works/category_sort.html', {"request": request, "works": works, 'projects': projects})

###END WORKS##########

#####CALBACK#######
@app.get('/callbackpage')
def callbackpage(request: Request, user = Depends(manager)):
    callback_all = callback_show()

    return templates.TemplateResponse('admin/callback.html', {"request": request,'callback_all': callback_all})

@app.get('/download_files')
def download_files(file, user = Depends(manager)):
    return FileResponse(file[1:], media_type="application/octet-stream")

@app.post('/del_callback_row/{row}', response_class= RedirectResponse, status_code=302)
def del_callback_row(row, user = Depends(manager)):
    del_callback_rowdb(row)
    return '/callbackpage'


###############LOGIN#########
@manager.user_loader()
def load_user(username:str):
    user = get_user(username)
    return user

@app.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    user = load_user(username)
    print(user.password)
    if not user:
        raise InvalidCredentialsException
    elif password != user.password:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data={"sub":username}
    )
    resp = RedirectResponse(url="/admin", status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp,access_token)
    return resp

@app.get("/private")
def getPrivateendpoint(user = Depends ( manager )):
    return "You are an authentciated user"

@app.get('/admin')
def admin(request:Request, user = Depends ( manager )):
    projects = show_project_all()
    category = show_category_all()
    cat = {cat.id:cat.name for cat in category}
    return templates.TemplateResponse('admin/admin.html', {"request": request, 'projects':projects, 'cat':cat})

@app.get('/login')
def loginwithCreds(request:Request):
    # request.session.values()
    return templates.TemplateResponse('admin/login.html', {"request": request})

