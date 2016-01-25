#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
taken from here
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

The 5 problems

(The following problems are ridiculously simple, but you'd be surprise to discover how many people struggle with them. To the point of not getting anything done at all. Seriously.)

Problem 1

Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

Problem 2

Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

Problem 3

Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

Problem 4

Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.

Update: Apparently this problem got a lot of people talking (although not as much as Problem 5 below.) You can click here to read my solution.

Problem 5

Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

"""


class problem_one(object):
	def __init__(self):
		self.input_list = input_list

	def for_loop_sum(self, input_list):
		sum_final = 0
		for x in enumerate(self.input_list):
			sum_final += self.input_list[x]
		return sum_final

	def while_loop_sum(self, input_list):
		sum_final = 0
		counter = 0
		while input_list[counter]:
			sum_final += input_list[counter]
			counter += 1
		return sum_final

	def recursive_sum(self, input_list):
		pass



lad = problem_one()
lad.input_list = [1,3]

nedd = lad.for_loop_sum
print nedd