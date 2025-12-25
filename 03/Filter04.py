# Write a program using filter() to find numbers greater than 50 from a list.

numbers=[1,2,67,69,105,50,51,49]
numbers_50=list(filter(lambda n:n>50,numbers))
print(numbers_50)
