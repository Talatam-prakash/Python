import os
from datetime import datetime
print(dir(os))   #all the attributes to access the modules

print(os.getcwd())  #print the present working location or directory

os.chdir("/home/prakash/Data science with python/class")  #change the location from in directory to another

print(os.getcwd())

print(os.listdir())   #return the all files and directories in the present location

os.makedirs("osmodule/Sub-ospython")  #makedirs create directories and sub dirctories at a time.

os.removedirs("osmodule/Sub-ospython")  #removedirs delete directories and sub dirctories.

os.mkdir('osmodule')   #mkdir create a single directories 

os.rmdir("osmodule")    #rmdir delete the directory

os.rename("matplot2.ipynb","matplotlib2.ipynb")    #change the directory or file names


print(os.stat("matplotlib2.ipynb"))    #return the files description like modification time , size, etc

print(os.stat("matplotlib2.ipynb").st_size)   #return the size of the file


mod_time=os.stat("matplotlib2.ipynb").st_mtime

print(datetime.fromtimestamp(mod_time))   # convert to understand time and date values


#walk the all directories,files inside the directory

for dirpath,dirname,filename in os.walk('/home/prakash/Data science with python/class/'):
    print("current path:",dirpath)
    print("dir name:",dirname)
    print("filename:",filename)
    print()

print(os.environ.get("HOME"))  #home directory

file_path=os.path.join(os.environ.get('HOME'),"test.txt")  #join the paths
print(file_path)

print(os.path.isdir(file_path)) #check whether it is directory or not


print(os.path.exists(file_path))     #check whether it exists or not

print(os.path.isfile("test.txt"))   #check whether it is file or not

print(dir(os.path))   #return all the function in os.path

print(os.path.basename("/tmp/test.txt")) # return basename of the path

print(os.path.splitext("/tmp/text.txt"))    #split the path before and after the txt