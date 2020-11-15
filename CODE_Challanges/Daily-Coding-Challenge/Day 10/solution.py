# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-09-07 21:21:30
# @Last Modified by:   prateek
# @Last Modified time: 2020-09-07 21:41:40

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters 
# as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

from queue import LifoQueue
string = 'AAAABBBCCDAA'
stack = LifoQueue(maxsize=len(string))
count=0
for i in range(len(string)):
	if stack.empty():
		stack.put(string[i])
		count+=1
	else:
		if string[i-1]==string[i]:			
			stack.put(string[i])
			count+=1
		else:
			print(count,end='')
			print(stack.get(),end='')

			while not stack.empty():
				stack.get()

			stack.put(string[i])
			count=1;
if not stack.empty():
	print(count,end='')
	print(stack.get(),end='')
