# Write a python program that uses reduce() to find the greatest common divisor (GCD) of the list of numbers.

from math import gcd
from functools import reduce
gcd_of_all=reduce(gcd,[12,18,24])
print(gcd_of_all)
