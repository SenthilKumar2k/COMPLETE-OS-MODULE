import os
from os import path

print(dir(path))                         #helps to know method in path class
files=os.listdir()

for file in files:                       #list of files and folder in current directory
    print(os.getcwd(),file)

for file in files:
    print(path.join(os.getcwd(), file))  #helps to join the folder or file with current path

for file in files:
    dir=path.join(os.getcwd(), file)
    if path.isdir(dir):                  #checking the path is folder or not (return boolean) 
        print("folder",dir)
    elif path.isfile(dir):               #checking the path is file or not (return boolean)
        print("File",dir)

for file in files:
    dir=path.join(os.getcwd(), file)
    print(path.split(dir))               #helps to split the path and file
    
for file in files:
    dir=path.join(os.getcwd(), file)
    print(path.split(dir)[1])            #split and display the files from folder and file
    print(path.split(dir)[0])            #split and display the path from folder and file

for file in files:
    dir=path.join(os.getcwd(), file)
    print(path.splitext(dir)) 

for file in files:
    dir=path.join(os.getcwd(), file)
    print(path.splitext(dir)[1])         #split and display the path + files and extension
    print(path.splitext(dir)[0])         #split and display the path + file