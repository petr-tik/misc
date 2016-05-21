#! /usr/bin/env python

# https://www.hackerrank.com/contests/may-world-codesprint/challenges/richie-rich

def local_maximise(number, length):
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
            if res[idx] == '9':
                continue
            else:
                if K - subs_needed > 1 and (is_changed[idx] or is_changed[end_idx]):
                    res[idx] = res[end_idx] = '9'
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