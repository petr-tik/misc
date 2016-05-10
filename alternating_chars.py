#! usr/bin/env python

# https://www.hackerrank.com/challenges/alternating-characters


def solve(s):
	last = s[0]
	deleted = 0
	for idx in xrange(1, len(s)):
		if s[idx] == last:
			deleted += 1
		else:
			last = s[idx]
	return deleted


N = int(raw_input())
for _ in xrange(N):
    s = raw_input()
    print solve(s)


print solve("AAAAAA")


