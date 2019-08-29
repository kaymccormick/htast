import sys
import argparse
import logging
import logging.config

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-filename')

    if not len(argv):
        argv = sys.argv[1:]
    args = parser.parse_args(argv)
    if args.input_filename:
        file = args.input_filename
    
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    

if __name__ == '__main__':
  main(sys.argv[1:])
