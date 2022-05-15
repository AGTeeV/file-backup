import os
import shutil

folderPath=input("enter folder path =>")
listOfFiles=os.listdir(folderPath)

for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(folderPath+"/"+ext):
        shutil.move(folderPath+"/"+file,folderPath+"/"+ext+"/"+file)
    else :
        os.makedirs(folderPath+"/"+ext)
        shutil.move(folderPath+"/"+file,folderPath+"/"+ext+"/"+file)