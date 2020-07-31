from os import getcwd
from sys import stdin, argv, path

path.append(getcwd())

from src.initialization.get_arguments import parse_argv, parse_stdin

from src.scrapers.scrape import concurrent_function
from src.scrapers.scrape import mk_request

from src.parsers.parse import parse_result


if __name__ == "__main__":
    urls = list()
    urls += parse_argv(input_argv=argv)
    urls += parse_stdin(input_stdin=stdin)
    if urls:
        results = concurrent_function(function=mk_request, args=urls, max_workers=50)
        concurrent_function(function=parse_result, args=results, max_workers=50)
