# Write a python program to handle a ZeroDivisionError.

try:
	a=int(input("Enter the dividend : "))
	b=int(input("Enter the divisor : "))
	result=a/b
	print("Result :",result)
except ZeroDivisionError:
	print("Error:Cannot divide by zero.")
except ValueError:
	print("Error:Enter only integers")
