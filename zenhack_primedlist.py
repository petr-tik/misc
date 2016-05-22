#!/usr/bin/env python

# https://www.hackerrank.com/contests/zenhacks/challenges/primedist

def isPrime(number):
    for x in xrange(2,int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True


def make_primes(top_limit):
    primes = []
    for num in xrange(2, top_limit+1):
        if isPrime(num):
            primes.append(num)
    return primes

def solve(N):
    popularities = [int(x) for x in raw_input().split()]
    primes = make_primes(N)
    entertainment = 0
    for idx, chap in enumerate(popularities):
        idx_prime = 0
        while idx_prime < len(primes) and primes[idx_prime] + idx < N:
            # print chap, popularities[idx], len(popularities)
            pair_entertainment = popularities[idx + primes[idx_prime]] - chap
            entertainment += pair_entertainment
            idx_prime += 1
    
    return entertainment


N = int(raw_input())
print solve(N)