#! usr/bin/env python
# -*- coding=utf-8 -*-
"""
codeforces 621a

Today, Wet Shark is given n integers. Using any of these integers no more than once, 
Wet Shark wants to get maximum possible even (divisible by 2) sum.
Please, calculate this value for Wet Shark.

Note, that if Wet Shark uses no integers from the n integers, the sum is an even integer 0.

Input
The first line of the input contains one integer, n (1 ≤ n ≤ 100 000). The next line contains n space separated integers given to Wet Shark. Each of these integers is in range from 1 to 10^9, inclusive.

Output
Print the maximum possible even sum that can be obtained if we use some of the given integers.

Sample test(s)
input
3
1 2 3
output
6

"""
def solve():
    n = int(raw_input())
    nums = map(int, raw_input().split())
    res = 0
    odds_sum = 0
    odd_min = -1
    odds_length = 0
    for new_num in nums:
        # add all even numbers to the sum
        if new_num % 2 == 0:
            res += new_num
        # new number is odd
        else:
            odds_length += 1
            odds_sum += new_num
            if odd_min == -1 or new_num < odd_min:
                odd_min = new_num

    res += odds_sum
    if odds_length % 2 == 1:
        res -= odd_min
    return res

print solve()


