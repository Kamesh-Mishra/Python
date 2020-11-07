# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-19 22:16:10
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-19 22:21:32

# PROBLEM (Google)

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

numbers = input().split()
k = int(input())
flag=0
for i in range(len(numbers)) :
	for j in range(i+1,len(numbers)):
		if (int(numbers[i]) + int(numbers[j])) == k:
			flag=1
			print('Yes {} + {} = {}'.format(numbers[i],numbers[j],k))
			
if flag==0:
	print('No there does not exist a pair of numbers for which the sum is equal to {}'.format(k))


# TIME COMPLEXITY : O(n^2)