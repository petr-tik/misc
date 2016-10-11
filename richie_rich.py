#! /usr/bin/env python

# https://www.hackerrank.com/contests/may-world-codesprint/challenges/richie-rich

def local_maximise(number, length):
    """ Function that takes number and its length and 
        returns 
            the int for how many values needed to change
            res (as array of digits)
            array of indices where the number has been changed
    """
    is_changed = [False for _ in number]
    res = [digit for digit in number]
    subs_needed = 0
    for idx in xrange(length/2):
        if res[idx] > res[-idx-1]:
            res[-idx-1] = res[idx]
            subs_needed += 1
            is_changed[-idx-1] = True
        elif res[idx] < res[-idx-1]:
            res[idx] = res[-idx-1]
            subs_needed += 1
            is_changed[idx] = True

    return subs_needed, res, is_changed 

def abs_maximise(subs_needed, res, is_changed, K, length):
    """ Uses local_maximise output 
        (subs_needed, res, is_changed and input K (number of changes allowed) 
        to maximise the number    
    """
    for idx in xrange(0, length):
        end_idx = length - idx - 1
        # if the number has odd number of digits, deal with the middle number
        if idx == end_idx:
            if res[idx] == '9':
                continue
            else:
                res[idx] = '9'
                subs_needed += 1

        else:
            if res[idx] == '9': # max abs value
                continue
            else:
                # if we still have subs and if either of the numbers has already been changed
                if K - subs_needed > 1 and (is_changed[idx] or is_changed[end_idx]):
                    res[idx] = res[end_idx] = '9'
                    # set them both to 9 (max digit) - it will count as 1 change
    return res


def solve():
    length, K = map(int,raw_input().split())
    number = raw_input()
    subs_needed, res, is_changed = local_maximise(number, length)
    if subs_needed > k:
        print "-1"
    res = abs_maximise(subs_needed, res, is_changed, K, length)
    print ''.join(res)

print local_maximise("14356", 5)
