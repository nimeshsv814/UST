# output for the given code

list=[1,2,3,4,5]
list[1:3]=[10,20]
print(list)       # answer would be [1,10,20,4,5]

print("============================================")
# to check whether the element exist or not

e=int(input("enter the element to check whether exists or not : "))
if e in list:
	print(e," is present in the list.")
else:
	print(e," is not present in the list.")

