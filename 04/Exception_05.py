# Write a program to handle multiple exceptions in a single try block.

try:
	a=int(input("enter dividend : "))
	b=int(input("enter divisor : "))
	result=a/b
	print("Result :",result)
except (ValueError,ZeroDivisionError) as e:
	print("error :",e)
