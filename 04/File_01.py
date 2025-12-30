# Write a python program to create a text file and write multiple lines into it.

f=open("sample01.txt","w")

f.write("hello world.\n")
f.write("file is created.\n")
f.write("lines were added.\n")

f.close()

print("file created and content added.")
