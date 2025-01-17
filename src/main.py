# A simple test
import logging
import sys

def main(args):
    for arg in args:
        logging.info(arg)

if __name__ == '__main__':
    main(sys.argv[1:])
