# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-30 22:11:34
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-30 22:12:20

# Question

# For a given n return the nth element in the binary sequence that does not containt any
# binary number containing the substring '11'.





import queue 
binary=[]
def generatePrintBinary(n): 

	# Create an empty queue 
	# from Queue 
	q = queue.Queue() 

	# Enqueue the first binary number 
	q.put("1") 

	# This loop is like BFS of a tree with 1 as root 
	# 0 as left child and 1 as right child and so on 
	while(n>0): 
		n-= 1 
		# Print the front of queue 
		s1 = q.get()
		if s1.find('11')==-1:
			# Since s1 does not 
			# contain 11 as a substring try all all other other permutations of the given number



			binary.append(s1)
			s2 = s1 # Store s1 before changing it 

			# Append "0" to s1 and enqueue it 
			q.put(s1+"0") 

			# Append "1" to s2 and enqueue it. Note that s2 
			# contains the previous front 
			q.put(s2+"1")
		else:
			# '11' has been detected so discard all the values that will be generated having 11 
			# increase the value of n as we will be discarding this entry
			n+=1



# Driver program to test above function
T = int(input())

for t in range(T):
	n = int(input())
	nums=[]
	for i in range(n):
		nums.append(int(input()))

	max_num = max(nums)
	generatePrintBinary(max_num)

	for i in nums:
		print(binary[i-1])



