#  While Loops

x = 0 
while x < 5:
	print("Counting:" , x)
	x +=1

y = 0
while y < 10:
	print("Counting:" ,y)
	y += 2


# Count Down

print("Count down")

count = 10
while count > 0:
	print(count)
	count -=1
print("Take off")

timer = 30
while timer > 10:
	print(timer, "wake up")
	timer -=1
	if timer == 15:
		print(timer , "go back to sleep")
		timer -=1
print("ahhh")


# for LOOPS

for letter in "hello":
	print(letter)



birthday  = input("what is your name")

for letter in birthday:
	print(letter)
	if letter == "A":
		print("I know him")
	else:
		print("ughh")
