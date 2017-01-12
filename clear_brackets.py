#! /usr/bin/env python3
"""

Given a string "((a)b((c)"
what is the min number of parens to remove (only remove) to make this a valid paren sequence

"""


def min_parens_remove(string):
    """ Input: string with 0 or more parenthesis
        Output: int - minimal number of parens we must remove 
    for the rest of the parens to be in correct order ()()()
    """
    stack = list()
    compl = {"(": ")", ")": "("}
    # to support different types of brackets
    #compl.update({"{": "}", "}": "{", "[": "]", "]": "["})
    print(compl)
    counter = 0
    for char in string:
        if char in compl:
            # only examine brackets
            if not stack or stack[-1] == char:
                # if the top of stack paren doesn't close the current char,
                # increment counter and add it to stack
                stack.append(char)
                counter += 1
            elif stack[-1] == compl[char]:
                # char closes current top of stack paren
                stack.pop()
                counter -= 1
    return counter

print(min_parens_remove("((a)b((c)"))
print(min_parens_remove("(((c)"))
print(min_parens_remove("(()"))
