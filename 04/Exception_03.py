# Write a program to open a file and handle a FileNotFoundError.

fileName=input("Enter the file name : ")

try:
	f=open(fileName,'r')
	content=f.read()
	print("File content:\n",content)
	f.close()
except FileNotFoundError:
	print("Error:File doesn't exist.")
