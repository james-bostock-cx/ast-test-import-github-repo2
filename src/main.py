import logging
import sys

# The following comment causes a low-severity vulnerability to be reported.
# password: S3cr3t

def main(args):
    for arg in args:
        logging.info(arg)

if __name__ == '__main__':
    main(sys.argv[1:])
