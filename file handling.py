# Opening a File():
#file = open("filename", "mode")
import os.path

file = open("example.txt", "r")

#Reading file():
file=open("example.txt",'r')
archana = file.read()
print(archana)
file.close()

#writing file()
file=open("example.txt","w")
file.write("my name is archana\n")
file.close

#appending a file():
file =open("example.txt","a")
file.write("this is an append mode")
file.close()

#closing a file:
file. close()

#cheacking if file exists:
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")
