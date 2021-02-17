#!/usr/bin/env python3
"""gameserial.

Usage:
gameserial.py --type=<type> <serial>

Options:
  -h, --help           Show this screen.
  -v, --version        Show version.
  -t, --type=<type>    Type of serial to parse.
                       Possible values:
                       nindisc-mfg - Nintendo GCN/Wii/Wii U
                                     manufacturing code
                       3ds-back    - Nintendo 3DS back of
                                     cart serial
  -i, --interactive    Interactive mode.


"""
from docopt import docopt
from sys import argv
import string
from datetime import datetime

error_invalid_len = 'Serial is the wrong length'

def parse_nindisc_mfg_serial(arguments):
    error_month_invalid_case = 'Month code is not uppercase'
    error_factory_notdigit = 'First character is not a digit'
    error_year_notdigit = 'Year is not a digit'
    
    input_stripped = arguments['<serial>'].strip()

    if len(input_stripped) != 8:
        raise ValueError(error_invalid_len)

    factory = input_stripped[0]

    if not factory.isdigit():
        raise ValueError(error_factory_notdigit)

    year_raw = input_stripped[1:3]
    if not year_raw.isdigit():
        raise ValueError(error_year_notdigit)
    
    year = int('20' + year_raw)

    if year < 2001:
        print('Warning: The year is before 2001. Is this correct?')
    if year > 2019:
        print('Warning: The year is after 2019. Is this correct?')

    #todo: finish adding checks
    
    if not input_stripped[3].isupper():
        raise ValueError(error_month_invalid_case)

    month = int(string.ascii_uppercase.index(input_stripped[3]) + 1)

    day = int(input_stripped[4:6])

    date = datetime(year, month, day)
    
    prodrun = input_stripped[6:8].lstrip('0')

    return({'Factory': factory,
            'Production Date': date.strftime('%d %B, %Y').lstrip('0'),
            'Production Run': prodrun})


def parse_3ds_back_serial(arguments):
    raise ValueError('Not implimented')
##    input_stripped = arguments['<serial>'].strip()
##
##    if len(input_stripped) != 10:
##        raise ValueError(error_invalid_len)
##
##    product_code = input_stripped[0:4]
##
##    month_code_to_month: {1:
##    
##    month_raw = input_stripped[4]
##
##    if not input_stripped[3].isupper():
##        raise ValueError(error_month_invalid_case)
##
##    month = int(string.ascii_uppercase.index(input_stripped[3]) + 1)
##
##    day = int(input_stripped[4:6])
##
##    date = datetime(year, month, day)
##    
##    prodrun = input_stripped[6:8].lstrip('0')
##    
##    return('Factory?: {}\nProduction Date: {}\nProduction Run?: {}\n'\
##    .format(factory,date.strftime('%d %B, %Y').lstrip('0'),prodrun))


def main(arguments):
    arg_to_function = {'nindisc-mfg': parse_nindisc_mfg_serial,
                       '3ds-back': parse_3ds_back_serial}
    for key, value in arg_to_function[arguments['--type']](arguments).items():
        print('{}: {}'.format(key, value))
    print()


if __name__ == '__main__':
    main(docopt(__doc__, version='gameserial'))
