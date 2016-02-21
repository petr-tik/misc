#!/usr/bin/env python
"""
You have to make a function that receives an array
of strings representing times of day (in the format "HH:MM") and returns the integer
number of minutes between the two closest times.

00:00 can be represented as either "00:00" or "24:00", and you can be guaranteed that all other inputs will fall in the range between 00:00 and 24:00. 

Constraints
2 <= Length of the array <= 1000

"""

class Solution(object):
	def __init__(self, array):
		self.array = array

	def adapt(self, string):
		# takes strings, returns an integer
		x = string.split(":")
		return ((60*int(x[0])+int(x[1])) % 1440)

	def make(self):
		minutes = [self.adapt(x) for x in self.array]
		minutes.sort()
		idx = len(minutes) - 1
		abs_diff = 2401
		while idx > 0:
			diff = minutes[idx] - minutes[idx - 1]
			if diff < abs_diff:
				abs_diff = diff
			idx -= 1

		print abs_diff



x = Solution(['5:12', '12:37', '12:12', '23:34', '23:30'])
x.make()