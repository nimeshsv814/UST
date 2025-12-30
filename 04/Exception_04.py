# Write a python program that uses try,except,else and finally blocks.

try:
	a=int(input("enter num1 : "))
	b=int(input("enter num2 : "))
	result=a/b
except ZeroDivisionError:
	print("Error:Can't divide by zero.")
except ValueError:
	print("Error:enter only integers.")
else:
	print("Result :",result)
finally:
	print("try,except,else,finally blocks used.")
