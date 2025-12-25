# Use filter() to extract all palindromic strings from a list.

strings=["level","hello","lol","madam","radio"]
palindromic_strings=list(filter(lambda s:s==s[::-1],strings))
print("Palindromic strings are",palindromic_strings)
