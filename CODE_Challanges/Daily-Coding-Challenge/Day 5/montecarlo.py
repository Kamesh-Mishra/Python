# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-23 22:06:54
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-23 22:10:05

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

# Solution

import random as rn
import math

num_darts_inside=0
num_darts_to_throw = 10000

for i in range(num_darts_to_throw):

	x = rn.random()**2
	y = rn.random()**2

	if math.sqrt(x+y) <1.0:
		num_darts_inside+=1

pi = float(num_darts_inside/num_darts_to_throw)*4
print('The value of pi is : {}'.format(pi))

