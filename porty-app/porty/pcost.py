#!/usr/bin/env python3
# pcost.py

from . import report

def portfolio_cost(filename):
    '''Computes the total cost of a portofolio via shares*price'''
    portfolio = report.read_portfolio(filename);
    return portfolio.total_cost

def main(argv):
    if(len(argv) != 2):
        raise SystemExit(f'Usage: {argv[0]} ' 'portfolio')
    print('Total cost:', portfolio_cost(argv[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)
