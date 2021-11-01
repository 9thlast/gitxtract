import argparse
import logging
from patterns import PATTERNS
from extractor import GitExtractor
from pygit2 import GitError


logger = logging.getLogger('gitxtract')


def cmd_all(args):
    r = args.regex
    if args.regex in PATTERNS:
        r = PATTERNS[args.regex]
    try:
        g = GitExtractor()
        for line in g.extract(r):
            print(line)
    except GitError as e:
        logger.error('current directory is not a git repository!')
        raise SystemExit

def init_logging(verbose=False):
    formatter = logging.Formatter(fmt='[%(asctime)s %(levelname)s] %(message)s', datefmt='%H:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    logger = logging.getLogger('gitxtract')
    logger.addHandler(handler)
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='gitxtract',
        description='extract strings from git repository histories'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='verbose',
        help='turn on debug logging'
    )
    subparsers = parser.add_subparsers()
    parser_all = subparsers.add_parser(
        'all',
        help='search for all matches of a regex in the history'
    )
    parser_all.add_argument(
        'regex',
        help='regex to use when searching'
    )
    parser_all.set_defaults(func=cmd_all)
    args = parser.parse_args()
    init_logging(args.verbose)

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
