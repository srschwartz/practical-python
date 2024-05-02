import os
import time

def follow(filename):
    '''
        Generic generator function
    '''
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

if __name__ == '__main__':   # Stock ticker using follow() to read the lines in portfolio.csv
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')