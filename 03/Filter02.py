# Write a program using filter() to select all words from a list that starts with a vowel.

fruits=["apple","pineapple","orange","kiwi","strawberry","lemon"]
vowel_fruits=list(filter(lambda f:f[0] in {'a','e','i','o','u'},fruits))
print(vowel_fruits)
