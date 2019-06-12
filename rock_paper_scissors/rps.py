#!/usr/bin/python

import sys

def rock_paper_scissors(n):
 options = ['rock', 'paper', 'scissors']
 base_case = 1
 result = []
 i = 0
 while n > base_case:
  # Iterate through the options
  # Permutations = factorials, so I have to generate the factorial of 3, where 1-3,
  # are attached to string values. 
  # The numbers are attached to these strings via the index of the options list.
 result.append([options[i]])



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')