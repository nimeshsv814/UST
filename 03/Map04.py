# Write a program using map() to calculate the length of each word in a list of strings.

words=["walter","jesse","mike","saul","gus","hector"]
length_words=list(map(lambda w:len(w),words))
print(length_words)
