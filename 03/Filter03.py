# Given a list of integers, use filter() to remove all negative numbers.

numbers=[2,-1,-45,67,89,-9,67]
negative_removed=list(filter(lambda x:x>=0,numbers))
print(negative_removed)
