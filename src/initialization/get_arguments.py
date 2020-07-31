from src.validations.validate import validate_web_url


def parse_argv(input_argv):
    urls = list()
    for url in input_argv[1:]:
        url = clean_url(url)
        if url and validate_web_url(url):
            urls.append(url)

    return urls


def parse_stdin(input_stdin) -> list:
    urls = list()
    for url in input_stdin:
        url = clean_url(url)
        if url and validate_web_url(url):
            urls.append(url)

    return urls


def clean_url(url: str) -> str:
    url = url.replace(' ', '')
    url = url.replace('\n', '')
    return url
