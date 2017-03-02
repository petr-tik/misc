#! /usr/bin/env python

""" Solution to the Word Machine problem 
with unittests at the bottom of the script

Given a Word Machine that takes commands:
int - pushes the int onto the stack 
POP - pops the top of the stack value
DUP - duplicates the top of the stack value
- - substracts the 2nd element from the top of the stack 
and pushes the results onto the stack
+ - pushes the sum of the 2 top elements onto the stack

Make a method solution, that takes a string of instruction and returns -1 for any errors 
or, if no errors, the top of the stack value after applying all the functions

run as below:
$ python word_machine.py
"""

import unittest


class Node(object):
    """ Node object for the Stack """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    """"Implementing a Stack as a LinkedList"""

    def __init__(self, arr=None):
        self.head = None
        self.size = 0
        if arr:
            for item in arr:
                self.push(item)

    def push(self, value):
        """Pushes a value on top of the stack
        returns nothing, just modifies the stack object"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            new_node.next = old_head
            self.head = new_node
        self.size += 1

    def pop(self):
        """Pops the value from the top of the stack,
        reduces the size counter on the object"""
        if self.head is None:
            return
        val = self.head.data
        self.head = self.head.next
        self.size -= 1  # reduce the size
        return val

    def top(self):
        """ Returns the top value without removing it """
        return self.head.data

    def as_list(self):
        """ Helper for debugging. Returns the Stack as a list
        with top of stack is at the start"""
        node = self.head
        res = []
        while node is not None and node.next is not None:
            res.append(node.data)
            node = node.next
        return res


def is_number_valid(num):
    """ Returns True if number inside agreed range """
    if 0 <= num < 2**20 - 1:
        return True
    else:
        return False


def is_integer(string):
    """ Returns true if the string consists of digits only, false otherwise"""
    return all(i.isdigit() for i in string)


def solution(S):
    """ Creates a new Stack object and applies word machine instructions to it
    Returns error code -1, if:
        integer overflow after addition/substraction
        not enough elements to pop
        not enough elements to duplicate, add, substract
        the stack is empty at the end

    Otherwise, returns the head of Stack after all operations
    """
    new_stack = Stack()
    for command in S.split():
        if is_integer(command):
            new_stack.push(int(command))

        elif command == "DUP":
            if new_stack.size > 0:
                x = new_stack.top()
                new_stack.push(x)
            else:
                return -1

        elif command == "POP":
            if new_stack.size > 0:
                x = new_stack.pop()
            else:
                return -1

        elif command == "+":
            if new_stack.size < 2:
                return -1
            else:
                x = new_stack.pop()
                y = new_stack.pop()
                res = x + y
                if is_number_valid(res):
                    new_stack.push(res)
                else:
                    return -1

        elif command == "-":
            if new_stack.size < 2:
                return -1
            else:
                x = new_stack.pop()
                y = new_stack.pop()
                res = x - y
                if is_number_valid(res):
                    new_stack.push(res)
                else:
                    return -1

    if new_stack.size == 0:
        return -1
    else:
        return new_stack.top()


class WordMachineTestCase(unittest.TestCase):

    def test_duplicate_on_empty(self):
        self.assertEqual(-1, solution("DUP"))

    def test_pop_on_empty(self):
        self.assertEqual(-1, solution("POP"))

    def test_push_only_one(self):
        val_to_push = 5
        res = solution("{}".format(val_to_push))
        self.assertEqual(val_to_push, res)

    def test_push_push_add(self):
        res = solution("10 10 +")
        self.assertEqual(res, 20)

    def test_push_push_substract_illegal(self):
        res = solution("15 10 -")
        self.assertEqual(res, -1)

    def test_push_add_too_few(self):
        res = solution("5 +")
        self.assertEqual(res, -1)

    def test_long_string(self):
        res = solution('13 DUP 4 POP 5 DUP + DUP + -')
        self.assertEqual(res, 7)


if __name__ == '__main__':
    unittest.main(verbosity=10)
