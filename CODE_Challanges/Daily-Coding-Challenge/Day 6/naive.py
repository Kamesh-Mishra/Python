# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-27 23:15:01
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-27 23:24:21


# This problem was asked by Google.

# A unival tree (which stands for "universal data") 
# is a tree where all nodes under it have the same data.

# Given the root to a binary tree, count the number of unival subtrees.

# Node Structure  
class Node: 
    # Utility function to create a new node 
    def __init__(self ,data): 
        self.data = data 
        self.left = None 
        self.right = None



def is_unival(root):
	return unival_helper(root,root.data)

def unival_helper(root,data):
	if root is None:
		return True
	if root.data==data:
		return unival_helper(root.left,data) and unival_helper(root.right,data)

def count_unival(root):
	if root is None:
		return 0
	left = count_unival(root.left)
	right = count_unival(root.right)
	return 1+left+right if is_unival(root) else left+right


root = Node(5) 
root.left = Node(4) 
root.right = Node(5) 
root.left.left = Node(4) 
root.left.right = Node(4) 
root.right.right = Node(5) 
# count_unival(root) 
print ("Count of Single datad Subtress is" , count_unival(root))



# This a naive solution as we are using the child twice once for its parent and one for the child himself.
# This can be improved by using bottom up approach i.e from child to parent