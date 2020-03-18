#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_prof = 0
  cur_max_price = 0
  cur_min_price = 0
  
  # So we want to loop through prices, and keep track of which one is the highest
  # once 
  for i in prices:
    if i > cur_max_price:
      cur_max_price = i
  for i in prices:
    if i < cur_max_price: #while?
      print(0)
  # return cur_max_price

print(find_max_profit([10, 7, 5, 8, 11, 9]))
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))