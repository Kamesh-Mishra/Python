# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-29 23:14:33
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-29 23:18:51


# Question 1D Peak Finder Problem

# Given an array of integers.
# Find a peak element in it. An array element is a peak if it is NOT smaller than its neighbours. 
# For corner elements, we need to consider only one neighbour.

# Solution


def peak_finder(arr,n):
	if n==1:
		return arr[n]
	
	if arr[0]>=arr[1]:
		return arr[0]
	elif arr[n-1]>=arr[n-2]:
		return arr[n-1]
	else:
		for i in range(1,n-2):
			if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
				return arr[i]


arr = [1, 3, 20, 4, 1, 0] 
n = len(arr) 
print("Index of a peak point is", peak_finder(arr, n)) 

# The following code is a naive solution for 1D-Peak Finder 
# TC : O(n)

