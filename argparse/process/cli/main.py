import logging
import argparse

log = logging.getLogger(__name__)


def main(args=None):

    parser = argparse.ArgumentParser(prog='process', description='Command line interface for the process package')
    parser.add_argument(
        '--loglevel', default='info', help='Log level',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
    )
    subparsers = parser.add_subparsers(help='Sub-commands')

    from .hello import add_subcommand_hello
    add_subcommand_hello(subparsers)

    from .calculate import add_subcommand_calc
    add_subcommand_calc(subparsers)

    # Parse all command line arguments
    args = parser.parse_args(args)

    # This is not a good way to handle the cases
    # where help should be printed.
    if hasattr(args, 'func'):
        # Call the desired subcommand function
        logging.basicConfig(level=args.loglevel.upper())
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0
