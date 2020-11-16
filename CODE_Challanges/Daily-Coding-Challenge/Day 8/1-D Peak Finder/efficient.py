# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-29 23:19:17
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-29 23:20:34


# Question 1D Peak Finder Problem

# Given an array of integers.
# Find a peak element in it. An array element is a peak if it is NOT smaller than its neighbours. 
# For corner elements, we need to consider only one neighbour.

# Solution
def findPeakUtil(arr, low, high, n): 
      
     # Find index of middle element 
     # (low + high)/2  
     mid = low + (high - low)/2 
     mid = int(mid) 
      
    # Compare middle element with its  
    # neighbours (if neighbours exist) 
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
        (mid == n - 1 or arr[mid + 1] <= arr[mid])): 
        return mid 
  
  
    # If middle element is not peak and  
    # its left neighbour is greater  
    # than it, then left half must  
    # have a peak element 
    elif (mid > 0 and arr[mid - 1] > arr[mid]): 
        return findPeakUtil(arr, low, (mid - 1), n) 
  
    # If middle element is not peak and 
    # its right neighbour is greater 
    # than it, then right half must  
    # have a peak element 
    else: 
        return findPeakUtil(arr, (mid + 1), high, n) 
  
  
# A wrapper over recursive  
# function findPeakUtil() 
def findPeak(arr, n): 
  
    return findPeakUtil(arr, 0, n - 1, n) 
  
  
# Driver code 
arr = [1, 3, 20, 4, 1, 0] 
n = len(arr) 
print("Index of a peak point is", findPeak(arr, n)) 