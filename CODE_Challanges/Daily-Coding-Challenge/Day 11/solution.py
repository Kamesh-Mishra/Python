# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2020-09-08 17:25:20
# @Last Modified by:   prateek
# @Last Modified time: 2020-09-08 17:34:04

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

def areParanthesisBalanced(expr) : 
    stack = [] 
  
    # Traversing the Expression  
    for char in expr: 
        if char in ["(", "{", "["]: 
  
            # Push the element in the stack  
            stack.append(char) 
        else: 
  
            # IF current character is not opening  
            # bracket, then it must be closing.   
            # So stack cannot be empty at this point.  
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return False
            if current_char == '{': 
                if char != "}": 
                    return False
            if current_char == '[': 
                if char != "]": 
                    return False
  
    # Check Empty Stack 
    if stack: 
        return False
    return True
  
  
# Driver Code 
if __name__ == "__main__" :  
    expr = "([)]";  
    if areParanthesisBalanced(expr) : 
        print("Balanced");  
    else : 
        print("Not Balanced");
