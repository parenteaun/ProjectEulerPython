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

def factor_finder(num, digitlength = 3):
	commondivisor = num
	factornum = 100

	while factornum < 999:
		if commondivisor % factornum == 0:
			commondivisor = commondivisor / factornum
			if len(str(factornum)) == digitlength and len(str(int(num / factornum))) == digitlength:
				# print(num, " ", int(num / factornum), " ", factornum)
				return num, int(num / factornum), factornum
				break
			else:
				# print(num, " does not work ", num / factornum, " ", factornum, " ", digitlength, " ", )
				factornum = 100
				return

		else:
			factornum += 1

for num in range (998001, 10000, -1):
	if palindromic_number(num):
		# print("yay", num, "is a palidrome")
		value = factor_finder(num, 3)
		if value != None:
			print(value)
			# break
