# Write a python program to count the number of lines,words,and
# characters in a text file.

f=open("sample01.txt","r")
line_count=0
word_count=0
char_count=0
for i in f:
	line_count=line_count+1
	words=i.split()
	word_count+=len(words)
	char_count+=len(i)

print("Lines :",line_count)
print("Words :",word_count)
print("Characters :",char_count)
