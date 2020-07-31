import warnings

from os import getcwd
from select import select
from sys import stdin, argv, path

from src.initialization.get_arguments import parse_argv, parse_stdin

from src.scrapers.scrape import concurrent_function
from src.scrapers.scrape import mk_request

from src.parsers.parse import parse_result


if __name__ == "__main__":
    """
    Nothing else than the main.py
    It'll make the main calls, like
    make the requests, and process
    their responses and output the
    result.
    """
    urls = list()
    urls += parse_argv(input_argv=argv)
    if select([stdin, ], [], [], 0.0)[0]:
        urls += parse_stdin(input_stdin=stdin)
    else:
        pass

    if urls:
        results = concurrent_function(function=mk_request, args=urls, max_workers=50)
        concurrent_function(function=parse_result, args=results, max_workers=50)
    else:
        warnings.warn(
            "No URL's given.\n The program is closing."
        )
