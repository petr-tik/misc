#! /usr/bin/env python

# string parser

# given a string with different types of brackets make sure each open bracket is closed

def parse(string):
    """Given a string of random chars and brackets, 
    return True if all brackets are opened and closed in the right order"""
    # the solution uses a stack for all the opening brackets. 
    # Keep pushing opening brackets onto the stack
    # when a closed bracket comes in, check if the top of the stack is its counterpart
    # if so, pop it off, else return False

    closed_brackets = ['}', ']', ')']
    open_brackets = ['{', '(', '[']
    counterparts = {'}':'{', ']':'[', ')':'('}
    stack = []    
    for idx, char in enumerate(string):
        if char in closed_brackets and not stack:
            return False
        if char in open_brackets:
            stack.append(char)
        if char in closed_brackets and stack:
            if stack[-1] == counterparts[char]:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True 


print parse(']]]')
print parse('(){}')
print parse('[]((]')
