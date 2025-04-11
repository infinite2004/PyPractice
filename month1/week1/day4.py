# Boolean Expressions & Condiotnal statements 

print(5 > 3)
print(4 == 4)
print(7 != 3)
print(3 < 1)

#Conditonal Statements 


age = int(input("What is your age")) 

if age  >= 18:
    print("can vote")
else:
    print("youre too young")


# Logical Operators

"""
and --> True if both are True --> ex: True and False --> False


or --> True if at least one is --> ex: True or False --> True


not --> inverts the value --> ex: not True --> False

"""

temp = int(input("what temperture do you like"))

raining  = False

if temp > 20 and not raining :
	print("Great day for a walk!")
else:
	print("Maybe stay in")

# Password checker

print("Practice: Password Checker")

correct_password = "aq"
attempts = 3

while attempts > 0:
	entered = input("Enter the password: ")
	if entered == correct_password:
		print("Access granted")
		break
	else:
		attempts -=1
		print(f"Wrong password. {attempts} attempts left")
	
	if attempts == 0:
		print("Access denied")	    
