# pcost.py
#
# Exercise 1.27


# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         print(row)
#         shares = int(row[1])
#         price = float(row[2])
#         total_cost += shares * price
#
# print('Total cost is', round(total_cost, ndigits=2))
import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for number, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print(f'Row {number}: Bad row: {line}')

        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost is', cost)