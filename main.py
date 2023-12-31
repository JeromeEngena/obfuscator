import sys
from argparse import ArgumentParser

import obfu


def main():
    print(obfu.lackofart)
    parser = ArgumentParser('python3 obfu.py')
    parser._action_groups.pop()

    # A simple hack to have required arguments and optional arguments separately
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Required Options
    required.add_argument('-s', '--str', help='String to obfuscate', dest='str')
    required.add_argument('-e', '--enc', help='Encoding type. eg: ibm037, utf16, etc', dest='enc')

    # Optional Arguments (main stuff and necessary)
    optional.add_argument('-ueo', help='URL Encode Output', dest='ueo', action='store_true')
    optional.add_argument('-udi', help='URL Decode Input', dest='udi', action='store_true')
    args = parser.parse_args()
    if not len(sys.argv) > 1:
        parser.print_help()
        quit()
    print('Input: %s' % args.str)
    print('Output: %s' % (
        obfu.paramEncode(params=args.str, charset=args.enc, urlDecodeInput=args.udi, urlEncodeOutput=args.ueo)))


if __name__ == '__main__':
    main()
