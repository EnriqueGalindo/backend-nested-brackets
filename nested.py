#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
import sys

__author__ = "Your Github Username"

def nested_brackets(line):
    openers = ('(', '[', '<', '{', '(*')
    closers = (')', ']', '>', '}', '*)')
    stack = []
    index = 0
    fail_safe=0
    
    while line:
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        elif line.startswith("*)"):
            token = "*)"
        if token in openers:
            stack.append(token)
        elif token in closers:
            if len(stack) == 0:
                print("No" + str(index))
                fail_safe = 1
                index += 1
                break
            elif stack[-1] == openers[closers.index(token)]:
                stack.pop()
            else:
                print("No" + str(index))
                fail_safe = 1
                index += 1
                break
        line = line[len(token):]
        index += 1
    if len(stack) == 0 and fail_safe == 0:
        print("Yes")
    elif fail_safe == 0:
        print("No" + str(index))
def main(args):
    with open(args, 'r') as document_text:
        text_string = document_text.readlines()
        for line in text_string:
            nested_brackets(line)


    


if __name__ == '__main__':
    main(sys.argv[1])
    
