# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-19 22:34:23
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-19 22:47:02

# This problem was asked by Uber.

# Given an array of integers, 
# return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].

# Solution
import numpy as np 

numbers = [int(num) for num in input().split()]
mul =0
temp= list()
count_zero = numbers.count(0)
if count_zero >=2:
	print([0] * len(numbers))
elif count_zero == 1 :
	index_zero = numbers.index(0)
	temp = [0] * len(numbers)
	temp[index_zero]= np.prod([num for num in numbers if num>0])
	print(temp)
else :
	mul = np.prod(numbers)
	for num in numbers:
		temp.append(int(mul/num))
	print(temp)
