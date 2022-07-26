#!/usr/bin/env python3
# report.py

from . import tableformat
from .portfolio import Portfolio
from .fileparse import parse_csv

def read_portfolio(filename, **opts):
    '''
    Read the portfolio into a list of dictionaries with keys,
    names, shares and price
    '''
    with open(filename, 'r') as lines:
        portfolio = Portfolio.from_csv(lines)
    return portfolio


def read_prices(filename):
    ''' Read prices from a csv file into a dictionary.
    Key would be the name of the stock, value is the price of the stock.'''
    lines = open(filename);
    portfolio = parse_csv(lines, types=[str, float], has_headers=False, silence_errors=False)
    return dict(portfolio)

def make_report(portfolio, price):
    report = []
    for stock in portfolio:
        name = stock.name
        shares = stock.shares
        price_in = stock.price
        try:
            price_out = price[name]
            price_change = price_out - price_in
        except:
            print('Cannot find the current stock price.')
        report.append((name, shares, price_out, price_change))

    return report

def print_report(report, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read the portfolio and price
    portfolio = read_portfolio(portfolio_filename)
    price = read_prices(prices_filename)

    # creating the report data
    report = make_report(portfolio, price)
    
    # print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if(len(argv) == 4):
        portfolio = argv[1]
        prices = argv[2]
        fmt = argv[3]
    else:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfolio prices fmt[OPTIONAL]')
    
    portfolio_report(portfolio, prices, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)