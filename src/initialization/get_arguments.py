from src.normalizers.normalize import clean_url


def parse_argv(input_argv: list) -> list:
    """
    Parse the arguments given by the terminal.
    :param input_argv: The arguments given
    :type input_argv: list
    :return: A list of valid URL's
    :rtype: list
    """
    urls = list()
    for url in input_argv[1:]:
        url = clean_url(url)
        urls.append(url)

    return urls


def parse_stdin(input_stdin) -> list:
    """
    Parse the arguments given by the terminal
    as a text file.
    :param input_stdin: The arguments given,
     from the file
    :return: A list of valid URL's
    :rtype: list
    """
    urls = list()
    for url in input_stdin:
        url = clean_url(url)
        urls.append(url)

    return urls
