'''
Title: Largest palindrome product

Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

'''
Background Review:
The smallest 3 digit numbers are 100. 100x100 = 10,000
The largest 3 digit numbers are 999. 999x999 = 998,001
We only need to traverse this range backwards and search for 3 digit factors.

Goal: Create a function to identify palidromic numbers
Goal: Create a function to then check for factors.
'''
	
def palindromic_number(num = 9009):
	# initialize empty lists
	l1 = []
	l2 = []
	# create a string out of the number
	stringify = str(num)
	length = len(str(num))
	''' 
	Using int() below truncates the decimal point for odd numbers of digits.
	for odd numbered digits the middle number doesnt matter for palindromes. 
	Simplifed the if condition down to a single line
	'''
	halfway = int(length / 2)
	#traverse 1st half
	for x in range(halfway):
		#create a list for comparison:
		l1.append(stringify[x])
	#traverse 2nd half backwards
	for y in range(length-1, halfway -1 , - 1):
	 	if len(l1) == len(l2):
	 		break
	 		#this prevent the middle number in Odd numbered digits from interfering with comparison
	 	else:
	 		l2.append(stringify[y])
	#compare the lists and return result
	if l1 == l2:
		return True
	else:
		return False

#digit length defaulted to 3
def factor_finder(num, digitlength = 3):
	commondivisor = num
	factornum = 999
	while factornum > 100:
		#check for solution
		if commondivisor % factornum == 0:
			# check to ensure the answer matches the digit length we are looking for.
			if len(str(factornum)) == digitlength and len(str(int(num / factornum))) == digitlength:
				#return the correct value
				return num, num / factornum, factornum
			else:
				#if both factors aren't 3 digits, factor out the factornum and restart the loop.
				commondivisor = commondivisor / factornum
				factornum = 999
		else:
			# the issue that was holding me up from solving was starting at the highest value factor and decreasing.
			factornum -= 1


for num in range (998001, 10000, -1):
	if palindromic_number(num):
		value = factor_finder(num, 3)
		if value != None:
			#print the answer then stop the loop
			print(value)
			break


'''
Congratulations, the answer you gave to problem 4 is correct.

The public tables currently show that this problem has been solved by 491461 members.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

Not enough data to determine solve metrics.
'''