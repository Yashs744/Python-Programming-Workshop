def unique_list(l):
	x = []
	for a in l:
	if a not in x:
		x.append(a)
	return x

print(unique_list_([1,2,3,3,3,3,4,5])) 