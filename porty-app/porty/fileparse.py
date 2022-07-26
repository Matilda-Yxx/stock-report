#!/usr/bin/env python3
# fileparse.py

import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',',silence_errors=False):
    '''
    Parse a CSV file into a list of records with the given select columns
    '''
    if isinstance(lines, str):
        raise RuntimeError('first input argument should be an iterable object')

    # check input args
    if select is not None and has_headers is False:
        raise RuntimeError("select argument requires column headers")
    
    rows = csv.reader(lines, delimiter=delimiter) 
    #! lines can be any object which supports the iterator protocol and returns a string each time its __next__() method is called — file objects and list objects are both suitable.

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering 
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue


        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
