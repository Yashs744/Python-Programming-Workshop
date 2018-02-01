# Loops in Python

## Example 1
for i in range(0, 10):
	print (i)

'''
	OUTPUT:
		0
		1
		2
		3
		4
		5
		6
		7
		8
		9
'''

## Example 2
for i in range(10, 0, -1):
	print (i)

'''
	OUTPUT:
	10
	9
	8
	7
	6
	5
	4
	3
	2
	1
'''

## Example 3
string_ = "A Random String"
for word in string_.split():
	print (word)

'''
	OUTPUT:
	A
	Random
	String
'''

## Example 4
words = "Python"
for char in words:
	print (char)

'''
	OUTPUT:
	P
	y
	t
	h
	o
	n
'''

## Example 5
names = ["Alex", "Bob", "Nancy"]
for name in names:
	print ("Name:", name)

'''
	OUTPUT:
	Name: Alex
	Name: Bob
	Name: Nancy
'''