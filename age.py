# Program to take age as input and display
# if we are eligible to drive or not

age = int(input("Enter your Age: "))

if age < 18:
	print ("Sorry! You Cannot Drive!!!")
else age >= 18:
	print ("You Can Drive!!!")