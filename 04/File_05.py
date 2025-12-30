# Write a python program to search for a specific word in a text file and
# display the line numbers where it appears.

f=open("sample01.txt","r")

word=input("enter the word to be searched : ")

line_no=0
word_found=False

for i in f:
	line_no+=1
	if word in i:
		print(f"Word - '{word}' is found in line number - '{line_no}'")
		word_found=True
if not word_found:
	print("word not found in the file.")
