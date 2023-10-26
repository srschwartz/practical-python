# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, types=None, select=None, has_headers=False, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # If select = True and has_headers = False, raise an error
        if select and not has_headers:
            raise RuntimeError("Select argument requires column headers")

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
        for rowno, row in enumerate(rows, 1):
            if not row:    # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]

            # Convert data to types specified, if there is a value error print the reason
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Could not convert Row {rowno}: {row}, for reason: {e}")
                    continue

            # Make a dictionary or a tuple depending on file structure
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float], select=['name', 'shares', 'price'], has_headers=True)
print(portfolio)