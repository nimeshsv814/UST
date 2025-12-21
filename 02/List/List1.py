# append() ==> function is used to add an element at the end of a list.

# del list_name[index] ==> is used to remove the element from list using index value.

# Examples :

list=[1,2,3]
list.append(4)  # 4 is added to list
list.append(5)  # 5 is added to list
print(list)  # answer would be [1,2,3,4,5]
del list[1]  # element with index 1 is removed(2 is removed),List would be [1,3,4,5]
del list[3]  # element with index 3 is removed(5 is removed),List would be [1,3,4]
print(list)  # answer would be [1,3,5]
