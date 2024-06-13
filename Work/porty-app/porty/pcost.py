# pcost.py
#
# Exercise 1.27

import csv
import sys
from .report import read_portfolio

def portfolio_cost(filename):
    '''
        Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s filename' % args[0])
    p = portfolio_cost(args[1])
    print('Total cost is: ', p)


if __name__ == '__main__':
    import sys
    main(sys.argv)


