#! usr/bin/env/ python

# https://www.hackerrank.com/challenges/the-time-in-words

h = int(raw_input()) # between 1 and 12 
m = int(raw_input()) # between 0 and 60

numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9:"nine", 10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty"
        }


def make_phrase(h, m):
    if m == 0: 
        print "{} o' clock".format(numbers[h])

    elif m == 15:
        print "{} past {}".format(numbers[15], numbers[h])

    elif m < 30:
        print "{} minutes past {}".format(mins_in_words, numbers[h])

    elif m == 30:
        print "half past {}".format(numbers[h])

    elif m == 45:
        print "{} to {}".format(numbers[15], numbers[h+1])

    elif m > 30:
        m_from_sixty = abs(m % -60)
        print "{} minutes to {}".format(numbers[m_from_sixty], numbers[h+1])


make_phrase(h, m)