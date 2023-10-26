# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    total_cost = 0.0
    f = read_portfolio(filename)
    for line in f:
        shares = line['shares']
        price = line['price']
        total_cost += shares * price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost is', cost)