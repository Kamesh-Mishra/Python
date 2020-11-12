# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-27 23:48:09
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-27 23:48:45


# This problem was asked by Airbnb.

# Given a list of integers, write a function that 
# returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, 
# ince we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def find_max_sum(arr): 
    incl = 0
    excl = 0
     
    for i in arr: 
          
        # Current max excluding i (No ternary in  
        # Python) 
        new_excl = excl if excl>incl else incl 
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return (excl if excl>incl else incl) 

arr = [5, 5, 10, 100, 10, 5] 
print (find_max_sum(arr)) 
