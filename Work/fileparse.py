# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, types=None, select=None, has_headers=False, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # If has_headers, read column headers
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        # If columns were selected, filter for selected columns
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]

            # Convert data to types specified
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary or a tuple depending on file structure
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv', types=[str, float], select=['name', 'shares'], has_headers=True)
print(portfolio)