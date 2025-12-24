def remove_duplicates(list):
	new_list=[]
	for i in list:
		if i not in new_list:
			new_list.append(i)
	return new_list

list=[1,1,2,2,77,7,7,8,10,11,11]
no_duplicates=remove_duplicates(list)
print(no_duplicates)
