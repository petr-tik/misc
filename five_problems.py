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

Write a function that computes the list of the first 100 Fibonacci numbers. 
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. 
The first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

Problem 4

Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.

Update: Apparently this problem got a lot of people talking (although not as much as Problem 5 below.) You can click here to read my solution.

Problem 5

Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

"""


class problem_one(object):
	def __init__(self, input_list):
		self.input_list = input_list

	def for_loop_sum(self):
		sum_final = 0
		for x in enumerate(self.input_list):
			sum_final += self.input_list[x[0]]
		print "the final sum is =", sum_final

	def while_loop_sum(self):
		sum_final = 0
		counter = 0
		# until the counter reaches the last element of the list
		while counter < len(self.input_list):
			sum_final += self.input_list[counter]
			counter += 1
		print "The final sum of list {} is".format(self.input_list), sum_final

	def recursive_sum(self, input_list):
		pass


sol_1 = problem_one([1,3,4])
sol_1.for_loop_sum()
sol_1.while_loop_sum()



class problem_two(object):
	"""
	input: 2 lists of possibly different lengths
		[a,b,c,d,e]
		[1,2,3]

	output:
	one list where members alternate
	[a, 1, b, 2, c, 3, d, e]
	"""
	
	def __init__(self, list1, list2):
		self.list1 = list1
		self.list2 = list2

	def merge_lists(self):
		final_list = []
		combined_list_length = len(self.list1) + len(self.list2)
		x = 0


		print "the merged list is", final_list

sol_2 = problem_two([1,2,3], [4,5,6])
sol_2.merge_lists()



class problem_three(object):
	"""outputs a list of first n Fibonacci numbers"""

	def __init__(self):
		pass
	def fib(self, n):
		if n <= 3:
			print results_list[:n]
		else:
			counter = 3
			results_list = [0, 1, 1]
			while counter < n:
				results_list.append(results_list[-2] + results_list[-1])
				counter += 1

			print results_list

sol_3 = problem_three()
sol_3.fib(10)








