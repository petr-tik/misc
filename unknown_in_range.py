"""
a Q from David Beck
Given an unsorted sequence of numbers in the range between x and y (eg 1..100) with just one number missing. 
Find a O(k) algorithm to calculate the missing value
"""

import random

class problem_range(object):
	def __init__(self, lower_bound, upper_bound):
		print "To make a range of numbers between 2 bounds, I need you to tell me the lower and upper bound"
  	
		self.lower_bound = lower_bound
  		self.upper_bound = upper_bound
  		if self.upper_bound <= self.lower_bound:
  			print "The upper bound has to be greater than the lower bound"

  		else: 
  			full_range = list(xrange(self.lower_bound, self.upper_bound))
	  		# delete random member
  			del full_range[random.randint(self.lower_bound, (self.upper_bound - 1))]
			print full_range



	def find_missing(self):
		missing = 0
		for x in xrange(self.lower_bound, self.upper_bound):
			pass
  		

lad = problem_range(3,5)

  
  


