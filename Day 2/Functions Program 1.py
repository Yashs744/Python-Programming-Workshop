def factorial(n):
	if n == 0 or n == 1:
		return n
	else:
		return n * factorial(n-1)

n = int(input("Input a number to compute the factiorial : "))
print(factorial(n))