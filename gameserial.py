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
  -i, --interactive    Interactive mode.


"""
from docopt import docopt
from sys import argv
import string
from datetime import datetime

str_invalid_len = 'Serial is the wrong length.'

def parse_nindisc_mfg_serial(arguments):
    str_month_invalid_case = 'Month code is not uppercase.'
    
    input_stripped = arguments['<serial>'].strip()

    if len(input_stripped) != 8:
        raise ValueError(str_invalid_len)

    #I'm not 100% sure that the first digit is "factory",
    #but it seems to line up between discs of the same
    #country of manufacturing (based on the "Made in Japan"
    #or "Made in USA" mould text).

    factory = input_stripped[0]

    year = int('20' + input_stripped[1:3])

    if not input_stripped[3].isupper():
        raise ValueError(str_month_invalid_case)

    month = int(string.ascii_uppercase.index(input_stripped[3]) + 1)

    day = int(input_stripped[4:6])

    date = datetime(year, month, day)
    
    prodrun = input_stripped[6:8].lstrip('0')
    
    return('Factory?: {}\nProduction Date: {}\nProduction Run?: {}\n'\
    .format(factory,date.strftime('%d %B, %Y').lstrip('0'),prodrun))

arg_to_function = {'nindisc-mfg': parse_nindisc_mfg_serial}

def main(arguments):
    print(arg_to_function[arguments['--type']](arguments))

if __name__ == '__main__':
    main(docopt(__doc__, version='gameserial'))
