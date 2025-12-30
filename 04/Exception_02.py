# Write a program that accepts user input and handles a valueError if the
# input is not an integer


try:
	x=int(input("Enter the integer : "))
	print("Integer entered :",x)
except ValueError:
	print("Error:Input is not a integer.")
