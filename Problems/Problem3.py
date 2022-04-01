'''
Title: Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# Value is what we are testing
value = 600851475143 
commondivisor = value
primefactor = 3
'''
This methodology is much more efficient than my initial attempt. 
Here we use factor trees to significantly reduce the time complexity
'''
# End the loop when the prime factor we are testing becomes greater than the divisor
while commondivisor > primefactor:
	if commondivisor % primefactor == 0:
		commondivisor = commondivisor / primefactor
	else:
		primefactor+=2
print(commondivisor, " ", primefactor)


'''
Congratulations, the answer you gave to problem 3 is correct.

The public tables currently show that this problem has been solved by 555326 members.

You have earned 1 new award:

Baby Steps: Solve three problems
'''