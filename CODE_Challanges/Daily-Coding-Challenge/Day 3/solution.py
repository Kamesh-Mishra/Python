# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-20 10:58:32
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-21 21:21:22


# This problem was asked by Stripe.

# Given an array of integers, 
# find the first missing positive integer in 
# linear time and constant space. 
# In other words, find the lowest positive integer 
# that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# SOLUTION


numbers = [int(num) for num in input().split()]

m = max(numbers)
if m <1:
	print(1)
elif m==1:
	print(2)
else:
	arr = [0]*m
	for num in numbers:
		if num >=1:
			arr[num-1]=1

	for i in range(len(arr)):
		if arr[i] ==0 :
			print(i+1)
			break;
