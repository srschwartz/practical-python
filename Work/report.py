# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename, **opts):
    with open(filename) as csv:
        p = parse_csv(csv,
                      types=[str, int, float],
                      select=['name', 'shares', 'price'],
                      has_headers=True,
                      **opts)
        portfolio = [Stock(**line) for line in p]
        return Portfolio(portfolio)

def read_prices(filename):
    with open(filename) as csv:
        return dict(parse_csv(csv, types=[str, float]))

def make_report(portfolio, prices):
    stonks = []
    for s in portfolio:
        name = s.name
        shares = s.shares
        price = prices[s.name]
        change = price - s.price
        line = (name, shares, price, change)
        stonks.append(line)
    return stonks

def print_report(data, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in data:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Make report
    report = make_report(portfolio, prices)

    # Print formatted report
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
        
def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)

