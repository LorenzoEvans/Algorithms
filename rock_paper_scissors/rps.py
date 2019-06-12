#!/usr/bin/python

import sys

def rock_paper_scissors(n):
 options = ['rock', 'paper', 'scissors']
 base_case = 0
 result = []
 i = 0
 while n >= base_case and i <= n:
  # Iterate through the options
  # Permutations = factorials, so I have to generate the factorial of 3, where 1-3,
  # are attached to string values. 
  # The numbers are attached to these strings via the index of the options list.
  result.append([options[i]])
  n -= 1
  i =+ 1
  # while, some conditional:
  # j = i(maybe n, or len(options))
  # result[j].append(options[i])

 return result


print(rock_paper_scissors(3))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')