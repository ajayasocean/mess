#!/usr/local/bin/python python

import os

file=os.path.bassepath"/Users/ajaysagar/ocean/mess/others/sample1.txt"


def find_anagram():
    with open(file, 'r') as reader:  # read mode
        text = reader.readlines()
        for line in text:
            print(line)


if __name__ == '__main__':
    find_anagram()

