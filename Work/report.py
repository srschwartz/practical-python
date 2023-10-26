# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint
from fileparse import parse_csv


def read_portfolio(filename):
    with open(filename) as csv:
        return parse_csv(csv, types=[str, int, float], select=['name', 'shares', 'price'], has_headers=True)

def read_prices(filename):
    with open(filename) as csv:
        return dict(parse_csv(csv, types=[str, float]))

def make_report(portfolio, prices):
    stonks = []
    headers = (f'{"Name":>10s} {"Shares":>10s} {"Prices":>10s} {"Change":>10s}')
    l = '---------- ---------- ---------- -----------'
    stonks.append(headers)
    stonks.append(l)
    for s in portfolio:
        name = s['name']
        shares = s['shares']
        price = prices[s['name']]
        change = price - s['price']
        line = (f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
        stonks.append(line)
    return stonks

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    for row in report:
        print(row)
        
def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)

