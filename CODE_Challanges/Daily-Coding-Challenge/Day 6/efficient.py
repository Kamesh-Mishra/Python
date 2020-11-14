# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-08-27 23:22:02
# @Last Modified by:   prateek
# @Last Modified time: 2020-08-27 23:23:30
class Node: 
    # Utility function to create a new node 
    def __init__(self ,value): 
        self.value = value 
        self.left = None 
        self.right = None


def count_unival_subtrees(root):
    count, _ = helper(root)
    return count


def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False


root = Node(5) 
root.left = Node(4) 
root.right = Node(5) 
root.left.left = Node(4) 
root.left.right = Node(4) 
root.right.right = Node(5) 
# count_unival(root) 
print ("Count of Single datad Subtress is" , count_unival_subtrees(root))