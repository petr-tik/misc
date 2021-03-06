#! usr/bin/env python
# -*- coding: utf-8 -*-

import random as rnd
from itertools import combinations_with_replacement, combinations


"""
taken from here
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

The 5 problems

(The following problems are ridiculously simple, but you'd be surprise to discover how many people struggle with them. 
To the point of not getting anything done at all. Seriously.)

Problem 1

Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

Problem 2

Write a function that combines two lists by alternatingly taking elements. 
Eg: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

Problem 3

Write a function that computes the list of the first 100 Fibonacci numbers. 
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. 
The first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

Problem 4

Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. 
Eg given [50, 2, 1, 9], the largest formed number is 95021.

Update: Apparently this problem got a lot of people talking (although not as much as Problem 5 below.) 
You can click here to read my solution.

Problem 5

Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) 
such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

"""


def rnd_list():
    return [rnd.randint(1, 100) for _ in xrange(rnd.randint(10, 20))]

rnd_list1 = rnd_list()
rnd_list2 = rnd_list()

print "Here are the 2 random lists:"
print rnd_list1
print rnd_list2

###############################

# 			problem 1         #

###############################
# solved 2/3


class problem_one(object):

    def __init__(self, inputL):
        self.inputL = inputL

    def for_loop_sum(self):
        sum_final = 0
        for x in self.inputL:
            sum_final += x
        print "the for loop sum of {} is".format(self.inputL), sum_final

    def while_loop_sum(self):
        sum_final = 0
        counter = 0
        # until the counter reaches the last element of the list
        while counter < len(self.inputL):
            sum_final += self.inputL[counter]
            counter += 1
        print "The while loop sum of list {} is".format(self.inputL), sum_final

    def recursive_sum(self, alist=None):
        if alist is None:
            alist = self.inputL
        res = 0
        if len(alist) == 1:
            return alist[0]
        else:
            res += alist[0] + self.recursive_sum(alist[1:])
        return res


print "##########################\n\nProblem 1\n\n"
sol_1 = problem_one(rnd_list1)
sol_1.for_loop_sum()
sol_1.while_loop_sum()
print "The recursive sum of list {} is".format(sol_1.inputL), sol_1.recursive_sum()

###############################

# 			problem 2         #

###############################
# solved


def map_lists(list1, list2):
    mapped_tups = map(None, list1, list2)
    results = []
    for x in mapped_tups:
        if x[0]:
            results.append(x[0])
        if x[1]:
            results.append(x[1])
    print results

print "##########################\n\nProblem 2\n\n"
map_lists(rnd_list1, rnd_list2)


###############################

# 			problem 3         #

###############################
# solved


def fib(n):
    print "This is a list of {} fibonacci numbers".format(n)
    results = [0, 1, 1]
    if n <= 3:
        print results[:n]
    else:
        counter = 3
        while counter < n:
            results.append(results[-2] + results[-1])
            counter += 1

        print results


print "##########################\n\nProblem 3\n\n"

fib(rnd.randint(1, 30))


###############################

# 			problem 4         #

###############################
# grrrrr

class problem_four(object):
    """
    Problem 4
    inputL 
    a list of non negative integers, 

    output:
    the largest possible number out of list of integers
    Eg given [50, 2, 1, 9], the largest formed number is 95021.
    [9, 91, 95, 9500, 937] """
# make a dictionary where key is first digit and the value list is sorted
# in ascending order.

    def __init__(self, inputL):
        self.inputL = inputL

    def split(self, num):
        # takes a number and splits it into subgroups of increasing digits
        # takes 1232356, returns [123, 23, 56]
        num_string = str(num)
        result = []
        start = 0
        for x in xrange(1, len(num_string)):
            if num_string[x] <= num_string[x - 1]:
                result.append(num_string[start:x])
                start = x

        result.append(num_string[start:])
        return result

    def compare(self, a, b):
        # use split function to break integers into lists of numbers
        sa = self.split(a)
        sb = self.split(b)

        # loop over the smallest list
        for x in xrange(min(len(sa), len(sb))):
            if sa[x] == sb[x]:
                continue
            elif sa[x] > sb[x]:
                return -1
            else:
                return 1
        # you got to the end of the loop without the results find which string
        # is longer
        return len(sa) - len(sb)

    def solve(self):
        return sorted(self.inputL, cmp=self.compare)


print "##########################\n\nProblem 4\n\n"

x = problem_four(rnd_list1)
y = x.solve()
print y

###############################

# 			problem 5         #

###############################
"""
Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) 
such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

[1,'p',2,'j',3,'m',4]


"""


class problem_five(object):

    def __init__(self):
        self.inputL = [x for x in xrange(1, 10)]

    def combs(self):
        # makes a list: len 3**8 with all possible combinations of -, + and
        # join
        combs = [x for x in combinations_with_replacement(['-', '+', '_'], 8)]
        return combs

    def insert(self, sign_combo):
        pass

    def calc(self, numbers, symbols):
        # takes a list of sign combinations and range(1,10)
        # insert signs, join the numbers and calcuate the result
        res = 0
        for symbol_idx in xrange(1, 16, 2):
            pass

        pass

    def solve(self):
        # finds which sign combos yield the needed result and adds them to the
        # list
        res = []
        # for x in sign_combs:
        # if self.insert_n_calc(x) = 100:
        # res.append()

        print res

print "##########################\n\nProblem 5\n\n"
five = problem_five()
print five.combs()
