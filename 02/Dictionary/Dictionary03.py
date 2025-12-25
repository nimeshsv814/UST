# Write a python function that merges two dictionaries.

def mergeDicts(dict1,dict2):
	dict1.update(dict2)
	return dict1
dict1={"name":"nimesh","age":21}
dict2={"nationality":"indian","gender":"male"}
print(mergeDicts(dict1,dict2))
