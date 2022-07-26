#!/usr/bin/env python3
#tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain text format.
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end='')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML style.
    '''
    def headings(self, headers):
        print('<tr>', end='') # no new line
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='') # no new line
        for r in rowdata:
            print(f'<td>{r}</td>', end='')
        print('</tr>')

class FormatError(Exception): # inherit from the Exception class
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % fmt)
    
    return formatter

def print_table(portfolio, columns, formatter):
    '''
    Print table using given columns
    '''
    formatter.headings(columns)
    for stock in portfolio:
        rowdata = [str(getattr(stock, colname)) for colname in columns]
        formatter.row(rowdata)