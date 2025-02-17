import logging
import sys

# password: S3cr3t

def main(args):
    for arg in args:
        logging.info(arg)

if __name__ == '__main__':
    main(sys.argv[1:])
