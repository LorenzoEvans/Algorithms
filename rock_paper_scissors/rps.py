#!/usr/bin/python

import sys

def rock_paper_scissors(n):
 options = ['rock', 'paper', 'scissors']
 base_case = 1
 while n > base_case:
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')