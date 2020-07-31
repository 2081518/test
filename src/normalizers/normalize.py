import phonenumbers


def normalize_phone_number_list(phone_list: list) -> list:
    """
    Retire None, '' and ' ' from the list.
    :param phone_list: A list of phone numbers
    :type phone_list: list
    :return: Phone list cleaned up
    :rtype: list
    """
    phone_list = list(filter(None.__ne__, phone_list))
    phone_list = list(filter(' '.__ne__, phone_list))
    phone_list = list(filter(''.__ne__, phone_list))
    return phone_list


def normalize_phone_number(number: str):
    """
    Normalize the phone number given.
    :param number: Phone number
    :type number: str
    :return: None or the number formatted
     as numobj
    """
    try:
        number = phonenumbers.parse(number)
        return phonenumbers.format_number(number, 1)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None


def normalize_url(host: str, url: str) -> str:
    """
    Normalize a URL.
    :param host: Host of the URL
    :type host: str
    :param url: The URL
    :type url: str
    :return: The URL with the host
    :rtype: str
    """
    if host[-1] == "/" and url[0] == "/":
        return host + url[1:]
    elif host[-1] != "/" and url[0] != "/":
        return host + "/" + url
    else:
        return host + url


def clean_url(url: str) -> str:
    """
    Clean up a URL with space and
    "\n" inside It.
    :param url: Some URL
    :type: str
    :return: The URL cleaned up
    :rtype: str
    """
    url = url.replace(' ', '')
    url = url.replace('\n', '')
    return url
