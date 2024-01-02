import os

print(os.system("ls"))                   #simple way to execute shell commands
print(os.system('date'))
x=os.popen("ls")                         #executed shell commands in the forms of object
print(x)                                 #to display the object
print(x.read())                          #to read object
x=os.walk(os.getcwd())                   #get the path,folders and files in the form of tuple
print(x)                                 #return the generator object
print(next(x))                           #next() helps to display the generator object

