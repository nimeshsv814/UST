# Write a python function that takes a dictionary and returns a list of keys that have values greater than 50.

def value_greater_than_50(myDict):
	return [k for k,v in myDict.items() if v>50]
myDict={'A':78,'B':56,'C':89,'D':33,'E':50,'F':67}
print(value_greater_than_50(myDict))
