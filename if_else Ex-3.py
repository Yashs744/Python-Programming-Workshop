# Nested if-else

name = input('What is your name? ')

# There we can provide any name that we want to check with
if name.endswith('Sharma'):
	if name.startswith('Mr.'):
		print ('Hello,', name)
	elif name.startswith('Mrs.'):
		print ('Hello,', name)
	else:
		print ('Hello,', name)
else:
	print ('Hello, Stranger')