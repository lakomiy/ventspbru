from typing import List

from fastapi import UploadFile
from pathlib import Path
def upload_file(folder: str, files: List[UploadFile], nameproject):
    path = Path(folder + '/' + nameproject.replace(' ', '_')).mkdir(parents=True, exist_ok=True)


    for file in files:
        namefile = file.filename.replace(' ', '_')
        with open(folder + '/' + nameproject.replace(' ', '_') + '/' + namefile, 'wb') as fl:
            while contents := file.file.read(1024 * 1024):
                fl.write(contents)

    pathlist = [f'/{folder}/'+ nameproject.replace(' ', '_') +'/' + i.filename.replace(' ', '_') for i in files]
    return pathlist