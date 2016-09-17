#! /usr/bin/env python


"""

https://www.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/

Fibbonacci base is when instead of binary the 1 or 0 shows how many times you take the fib number of this index

dec 8 = 10110 in fib

Write a converter that takes base (dec or fib) and returns the number in the other base

"""

def fib(n):
    """ Given a number, generate a fibonacci sequence of length n with the greatest element at the front"""
    ret = [0, 1, 1]
    if n <= 3:
        return ret[:n]
    counter = 3
    while counter < n:
        ret.append(ret[-1] + ret[-2])
        counter += 1
    return ret[::-1]


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib_to_dec(num):
    """Takes a string in fibonacci base in form 100010 and converts it to decimal value """
    fib_seq = fib(len(num))
    res = 0
    for idx, item in enumerate(num):
        print int(item), fib_seq[idx]
        res += int(item) * fib_seq[idx]

    return res

def helper(num, fib_values, digits):
    """ Helper function for dec_to_fib. 
    Takes: 
    the number we need to convert to fib_base, 
    values of fibonacci sequence relevant to the number (less than or equal to) 
    the array of digits 

    Returns 
"""
    if num in fib_values:
        digits[fib_values.index(num)] = 1

    
    return digits

def dec_to_fib(num):
    """ Takes a decimal number (type int) and returns a string with its Fibonacci base representation.
    Method: generate fibonacci numbers until 
 """
    fib_gen = fib_generator()
    fib_values = []
    fib_num = fib_gen.next()
    while fib_num <= num:
        fib_values.append(fib_num)
        fib_num = fib_gen.next()

    fib_values.reverse() # turns it into human maths (left to right)
    digits = [0 for x in fib_values]



def convert(num, base_in, base_out):
    """ Given a number and its base, return the number in base_out """
    if base_in == "fib" and base_out == "dec":
        pass
        

def solve():
    inp = raw_input().split()
    base, num = inp[0], int(inp[1])

print fib(2)
print fib(8)
print fib_to_dec("1000000000")
print dec_to_fib(21)
