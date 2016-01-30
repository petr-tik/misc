"""
a Q from David Beck
Given an unsorted sequence of numbers in the range between x and y (eg 1..100) with just one number missing. 
Find a linear algorithm to calculate the missing value
"""

######################################################
# solution 1

import random

class problem_range(object):
	def __init__(self, lower_bound, upper_bound):
		
		self.lower_bound = lower_bound
  		self.upper_bound = upper_bound
  		self.full_range = list(xrange(self.lower_bound, self.upper_bound))
	  	# delete random member
  		del self.full_range[(random.randint(self.lower_bound, (self.upper_bound - 1))) - lower_bound]


	def find_missing(self):
		missing = sum(xrange(self.lower_bound, self.upper_bound))
		for x in self.full_range:
			missing -= x

		print "{} is missing from {}".format(missing, self.full_range)
  		

lad = problem_range(3,10)

lad.find_missing()


######################################################
# solution 2


"""
assign all value to hash table
use the numbers in the range (number - 1)

as keys to another list, where you can mark 

[1,2,4,5,6] - 3 missing
[1,1,1,0,1,1] - 



"""

  
  


