'''
Title: Even Fibonacci numbers

Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''

'''
With this problem I intend to practice pandas dataframes (df) and lists.
Idea: Load all the Fibonacci sequence values I need into a df then filter that df for processing
'''

import numpy as np
import pandas as pd

Fs = [1,2]
lastIdx = 1
x = 0

while Fs[lastIdx-1] + Fs[lastIdx] < 4000000:
	# Compute the next Fibonacci Number
	x = Fs[lastIdx-1] + Fs[lastIdx]
	# Add the new value to the list
	Fs.append(x)
	# Set the next index value for the list
	lastIdx = len(Fs) - 1

#Fibonacci sequence complete

df = pd.Series(Fs)

print(df)