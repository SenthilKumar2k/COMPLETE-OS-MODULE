import os

print(dir(os))        #list of methods in os module
print(os.getcwd())    #display the current working directory
print(os.listdir())   #list of files and folders in current directory
print(os.listdir("/home/pganalytics/Documents"))   #list of files and folders in given directory
os.chdir("/home/pganalytics/Documents/OS_Module")     #change the directory from current to given
print(os.getcwd())
os.mkdir("dir1")                        #to create a new directory
print(os.listdir())
os.rmdir("dir1")                        #to delete the exist directory
print(os.listdir())
#os.remove("osm.py")                    #to remove the file from the current directory
#print(os.listdir())
#os.rename("DEMO","demo")                #to change the directory name
#print(os.listdir())
print(os.stat("os_basics.py"))           #hepls to get the details about the file
print(os.stat("os_basics.py").st_size)   #helps to get the size of file in form of bytes