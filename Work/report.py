# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        return portfolio


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
        return prices

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

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

