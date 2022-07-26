#!/usr/bin/env python3
#follow.py

import csv
from .follow import follow
from . import report, tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    rows = (dict(zip(headers, row)) for row in rows)
    return rows

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def filter_symbols(rows, names):
    rows = (row for row in rows if row['name'] in names)
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    
    # print the ticked data
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        rowdata = [ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] #! must use double quotation marks here since there are single quotation marks within
        formatter.row(rowdata)

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)