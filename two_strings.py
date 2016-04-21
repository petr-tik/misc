#! usr/bin/env python

def common_string(word1, word2):
    letters_in_words = {}
    for char in word1:
        letters_in_words[char] = True

    for char in word2:
        if char in letters_in_words:
            return "YES"
    return "NO"
    

T = int(raw_input())
for x in xrange(T):
    word1 = raw_input()
    word2 = raw_input()
    print common_string(word1, word2)    
    for word in answers:
        print word
