'''
	LISTS IN PYTHON
'''

# 1. To Create Lists in Python
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Names = ['Alex', 'Bob', 'Nancy']

## List can have elements with different data type
list_1 = [1997, 1998, 'Alex', 'Bob', True, False, 3.45, 5.6]
## List-of-List
list_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2. To Print (display) elements in the list
## (i). using print statement
print (Numbers)
print (Names)

## (ii). using for loop
for num in Numbers:
	print (num)

print ()

for name in Names:
	print (name)

# 3. Methods available in Lists
'''
	.append(value) - appends element to end of the list
	.count('x') - counts the number of occurrences of 'x' in the list
	.index('x') - returns the index of 'x' in the list
	.insert('y','x') - inserts 'x' at location 'y'
	.pop() - returns last element then removes it from the list
	.remove('x') - finds and removes first 'x' from list
	.reverse() - reverses the elements in the list
	.sort() - sorts the list alphabetically in ascending order, or numerical in ascending order
'''
Numbers.append(11)
Numbers.append(12)

## Now Numbers is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 4. List Slicing
## Lists have a very nice property i.e slicing
## To slice a list we use list_name[start:end:step]
## start -> Starting Point (Inclusive), end -> Ending Point (Exclusive) & step -> Number of Steps to take

print (Numbers[::2]) # Starting till Ending with a step size of 2
## Output: [1, 3, 5, 7, 9, 11]
print (Numbers[::-1]) # Print whole list in reverse order
## Output: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

## To Access elements from the end we use -1, -2, -3 ... 
print (Numbers[-3:])
## Output: [10, 11, 12]

print (Numbers[-1:-4:-1])
## Output: [12, 11, 10]

# 4. Deleting elements from the list
## Delete 2nd value in Numbers
del Numbers[2]

## Delete Whole List
del Numbers[:]