import getopt
import platform
import logging
import os
import sys
from .version import script_name, __version__
from .extractor import *
from .importor import *
from .common import setup_custom_logger

setup_custom_logger('root')

_options = [
    'help',
    'version',
    'force',
]

_short_options = 'hVf'

_help = f"Usage: {script_name} [OPTION]... [URL]..."

def main(**kwargs):
    logging.debug(f'Welcome to {script_name}')
    opts = {}
    args = {}
    try:
        opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
    except getopt.GetoptError as e:
        logging.error(f"Invalid option! Try {script_name} --help' for more options.")

    if not opts and not args:
        print(_help)
    else:
        conf = {}
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                # Display help.
                print(_help)
            elif opt in ('-V', '--version'):
                # Display version.
                print("tmdb-import:")
                print("    version:  {}".format(__version__))
                print("    platform: {}".format(platform.platform()))
                print("    python:   {}".format(sys.version.split('\n')[0]))
        
    if args:
        url = args[0]
        if url.__contains__("www.themoviedb.org"):
            import_from_url(url)
        else:
            extract_from_url(url)

if __name__ == '__main__':
    main()