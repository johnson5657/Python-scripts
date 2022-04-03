import os

#os.remove("2222.txt") # delete a file from the disk
#os.rename("2222.txt","3333.txt") # rename a file name

os.path.exists("2222.txt") # checking if certain exists or not return  True \ False  help us before we remove a file or rename it

print(os.path.getsize("2222.txt")) # will get us back the file size in bytes


#checking if file exists
import os
import  datetime
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")


#the abspath function takes a file name and return its absoulte path
print(os.path.abspath("2222.txt"))
print(os.getcwd()) # print the current directory where the script is currently running from
print(os.mkdir("Python Dir")) # create new dir
os.chdir("Python Dir") # this will change directory(cd) to the directory we want to work in
os.path.getmtime("2222.txt") # will return the file creating time this will return an EPOCH time  we need convert is using datetime
datetime.datetime.fromtimestamp(os.path.getmtime("2222.txt")).strftime('%Y-%m-%d %H:%M:%S')
os.listdir("Python Dir") # return a list of all files and directories in a given dir
os.rmdir("Python Dir") # remove directory function will not remove the directory if the dir have files init

for name in os.listdir("C:\\"):
    fullname = os.path.join("C:\\",name) # join function will join each directory to the file name giving us the dir + file
    print(fullname)
    if os.path.isdir(fullname): # check if its directory or file return true\false for directory
        print("{} is a dir".format(fullname))

# using the join function will let us work with the script on diffrent OS systems as in Windows and Linux the speration is done with diffretn slash and backslash