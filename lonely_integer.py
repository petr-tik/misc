#!usr/bin/env python

# https://www.hackerrank.com/challenges/lonely-integer

def find_lonely(array):
    if len(array) == 1:
        return array[0]
    else:
        res = []
        res.append(array[0])
        for idx in xrange(1, len(array)):
            if array[idx] in res:
                res.remove(array[idx])
            else:
                res.append(array[idx])
        return res[0]


if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print find_lonely(b)