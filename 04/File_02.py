# Write a program to read the contents of a text file line by line.

f=open("sample01.txt","r")

for i in f:
	print(i)
f.close()
