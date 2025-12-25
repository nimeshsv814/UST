# Given a list of temperatures in celsius,use map() to convert them to Fahrenheit.

celsius=[2,19,27,31]
fahrenheit=list(map(lambda c:(c*1.8)+32,celsius))
print(fahrenheit)
