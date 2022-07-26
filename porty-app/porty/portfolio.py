#!/usr/bin/env python3
#portfolio.py

from . import fileparse, stock

class Portfolio:
    
    def __init__(self):
        self.holdings = []
    
    def append(self, holdings):
        if not isinstance(holdings, stock.Stock):
            raise TypeError('Expected a stock instance')
        self.holdings.append(holdings)
    
    @classmethod # Class methods are most often used as a tool for defining alternate constructors
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)
        for d in portdicts:
            self.append(stock.Stock(**d))
        return self

    def __iter__(self):
        return self.holdings.__iter__()
    
    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, index):
        return self.holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self.holdings)

    @property # such that you can do portfolio.total_cost without parentheses
    def total_cost(self):
        return sum(s.cost for s in self.holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self.holdings:
            total_shares[s.name] += s.shares
        return total_shares