# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-22 22:22:13
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-22 22:32:03


# Given an array of length n of non zero integers ordered in ascending order,
#  replace all duplicates with 0 and also return the effective size of the array. 

# Example : 

# Input : 2|2|4|4|7|32|32|47
# Output : 2|4|7|32|47|0|0|0 
# 		 Effectie Size = 5

# Solution :

numbers = [int(num) for num in input().split('|')]
result = []
count_dup=0
for num in numbers:
	if str(num) not in result:
		result.append(str(num))
	else:
		count_dup+=1

result = result + [str(0)]*count_dup

print('|'.join(result))
print('Effectie Size :',len(result)-count_dup)