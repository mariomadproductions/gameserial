#!/usr/bin/python3

from sys import argv
import string
from datetime import datetime

str_help = 'Pass the mastering code as the argument, ' \
           'or to use interactive mode, pass \'-i\' instead.'
str_invalid_mstr_len = 'Mastering code is the wrong length.'
str_invalid_mstr_case = 'Month code is not uppercase.'

def print_decoded_mstr(input_var):
    input_striped = input_var.strip()

    if len(input_striped) != 8:
        raise ValueError(str_invalid_mstr_len)

    factory = input_striped[0]

    year = int('20' + input_striped[1:3])

    if not input_striped[3].isupper():
        raise ValueError(str_invalid_mstr_case)

    month = int(string.ascii_uppercase.index(input_striped[3]) + 1)

    day = int(input_striped[4:6])

    date = datetime(year, month, day)
    
    prodrun = input_striped[6:8].lstrip('0')
    
    print('Factory: {}\nProduction Date: {}\nProduction Run: {}'\
    .format(factory,date.strftime('%d %B, %Y').lstrip('0'),prodrun))

def interactive_mode():
    while True:
        print_decoded_mstr(input('Input: '))

def main():
    try:
        arg = argv[1]
        if arg == '-i':
            interactive_mode()
        elif arg == '--help':
            print(str_help)
        else:
            print_decoded_mstr(arg)
    except IndexError:
        return


if __name__ == '__main__':
    main()
