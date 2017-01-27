"""
drw IV puzzle
Give an int N,
return the number of digits of 11^N that are '1' 
(O(n) space and time required)  
"""

from math import factorial


def number_of_ones(power):
    # brute force
    res = 0
    for char in str(11**power):
        if char == '1':
            res += 1
    return res


def nCr(n, k):
    """ Calculate the binomial coefficient"""
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

print(nCr(5, 3))

""" 11^N = (10+1) ... (10+1) - n times 
    let's look at 11^power as (1 + 10)^power
which expands
nCr(power, 0)*10^0 + nCr(power, 1)*10^1

this is a sequence of increasing powers of 10 and nCr for different values of r

"""


def number_of_ones2(power):
    res = 0
    for r in range(power + 1):
        if str(nCr(power, r))[0] == '1':
            print(str(nCr(power, r)))
            res += 1
    return res


for i in range(50):
    print(11**i, number_of_ones(i), number_of_ones2(i))
