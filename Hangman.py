import random

name = input("Enter your name")
print("Hello ", name)
print("we start with our game")

words = ["shubham","swapnil","harshal"]

word = random.choice(words)

guesses = ''

turns = 10

while turns > 0:

	failed = 0
	for char in word:

		if char in guesses:
			print(char)
		else:
			print("_")
			failed += 1

	if failed == 0:
		print("you won")
		print("word is ", word)

	guess = input("Enter a alphabet")
	
	guesses += guess
	
	if guess not in word:
		turns -= 1

		print("your turns remain ", turns)
		break


			

