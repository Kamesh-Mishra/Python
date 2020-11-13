# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-23 22:22:02
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-23 22:23:01

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.






import time
def scheduler(f,n):
    time.sleep(n/1000)
    f()

def hello_world():
    print("Hello World")

scheduler(hello_world,10000)