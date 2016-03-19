#! usr/bin/env python

first, second, N = map(int,raw_input().split())

def func_fact(idx, first, second):
    # funky fibonnaci, takes the first 2 values and returns value index idx
    # T(n) = (T(n-1))**2 + T(n-2)
    results = [first, second]
    counter = 2
    while counter < idx:
        next = (results[counter-1])**2 + results[counter - 2]
        results.append(next) 
        counter += 1
     
    return results[idx-1]


print func_fact(N, first, second)