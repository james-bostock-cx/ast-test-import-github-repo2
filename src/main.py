import logging
import sys

# Another comment
# The following comment causes a low-severity vulnerability to be reported.
# password: S3cr3t
# password: Chang3M3

def main(args):
    for arg in args:
        logging.info(arg)

if __name__ == '__main__':
    main(sys.argv[1:])
