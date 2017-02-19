"""
Find longest substring with unique characters in O(n) time.

co: bloomberg
status: done
"""

import string

example1 = string.ascii_lowercase
example2 = "bacabacaddolz"
example3 = "aaaaaaaa"


def longest_substr(big_string):
    """ Input:
            ascii string
        Returns:
            length
            longest substring of unique characters
    """
    res = 1
    if len(big_string) == 1:
        return res
    left_ptr = 0
    right_ptr = 1
    uniq_letters = list(big_string[left_ptr])
    while right_ptr < len(big_string):
        if big_string[right_ptr] not in uniq_letters:
            uniq_letters.append(big_string[right_ptr])
            res = max(res, right_ptr - left_ptr + 1)
            right_ptr += 1
            continue
        elif big_string[left_ptr] == big_string[right_ptr]:
            left_ptr = right_ptr
            right_ptr = left_ptr + 1
            try:
                uniq_letters = list(big_string[left_ptr])
                continue
            except:
                break
        else:  # char at right_ptr is already in set
            left_ptr = right_ptr - 1
            uniq_letters = list(big_string[left_ptr])

    return "".join(uniq_letters)


def test():
    print(longest_substr(example1) == example1)
    print(longest_substr(example2) == "dolz")
    print(longest_substr(example3) == "a")


test()
