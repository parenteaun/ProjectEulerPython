'''
Title: Multiples of 3 or 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
FoundNumbers = 0

# For loop up to 1000, the range function starts at 0
for x in range(1000):
	# Search for numbers with divisors with no remainders
	if x / 3 == int(x/3) or x / 5 == int(x/5):
		# Add a found number to the p

		FoundNumbers = FoundNumbers + x

print(FoundNumbers)

'''
Congratulations, the answer you gave to problem 1 is correct.

The public tables currently show that this problem has been solved by 967995 members.

This problem has a difficulty rating of 5%. The highest difficulty rating you had previously solved was 0%. 
This is a new record. Well done!

Not enough data to determine solve metrics.
'''