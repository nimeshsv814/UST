# Write a program to copy the contents of one text file into another file.

f_read=open("sample01.txt","r")
f_write=open("sample02.txt","w")

content=f_read.read()
f_write.write(content)

f_read.close()
f_write.close()
