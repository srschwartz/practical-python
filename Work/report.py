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
        for number, row in enumerate(rows, start=1):
            rec = dict(zip(headers, row))
            holding = {'name': row['name'], 'shares': int(row['shares']), 'price': float(row['price'])}
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


# total_cost = 0.0
# for line in portfolio:
#     total_cost += line['shares'] * line['price']
#
# current_value = 0.0
# for line in portfolio:
#     n = line['name']
#     current_value += line['shares'] * prices[n]
#
#
# print('Original cost', total_cost)
# print('Current value', current_value)
# gain = current_value - total_cost
# print('Gain', gain)
# if gain > 0:
#     print('Hooray!')
# else:
#     print('Oh no')

def make_report(portfolio, prices):
    stonks = []
    for s in portfolio:
        name = s['name']
        shares = s['shares']
        price = prices[s['name']]
        change = price - s['price']
        line = (name, shares, price, change)
        stonks.append(line)
    return stonks

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
l = '---------- ---------- ---------- -----------'

print('%10s %10s %10s %10s' % headers)
print(l)
for name, shares, price, change in report:
    p = str('%0.2f' % price)
    print(f'{name:>10s} {shares:>10d} {("$" + p):>10s} {change:>10.2f}')