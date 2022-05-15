import os
import shutil

source=input("enter the source folder=>")
destination=input("enter destination=>")
source=source+"/"
destination=destination+"/"
files=os.listdir(source)

for file in files:
    shutil.copy((source+file),destination)