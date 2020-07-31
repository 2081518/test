from urllib.parse import urlparse
import phonenumbers
import re


def validate_url_incomplete(url: str) -> bool:
    """
    Validate if the URL has or not some host.
    :param url: URL complete or not
    :type url: str
    :return: True if the URL is without a host
     and False if It has the host.
    :rtype: bool
    """
    pattern = r"http[s]?:\/\/(?:www\.)?([\w]+)\."
    if len(re.findall(pattern, url)) > 0:
        return False
    else:
        return True


def validate_web_url(url: str) -> bool:
    """
    Validate if the URL is a valid and
    complete URL.
    :param url: URL complete or not
    :type url: str
    :return: True if the URL is valid
     and False if is not.
    :rtype: bool
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def validate_image(supposed_image: str) -> bool:
    """
    Validate if the URL the image is in fact an
    image or not, through the extension of the
    URL.
    :param supposed_image: URL of the image
    :type supposed_image: str
    :return: True if It has some of the extensions
     and False if It doesn't have.
    :rtype: bool
    """
    if '.png' in supposed_image:
        return True
    elif '.jpg' in supposed_image:
        return True
    elif '.jpeg' in supposed_image:
        return True
    elif '.ico' in supposed_image:
        return True
    else:
        return False


def validate_phone(supposed_phone: str) -> bool:
    """
    Validate if the phone number given is valid
    or not.
    :param supposed_phone: Phone number
    :type supposed_phone: str
    :return: True if the phone number is valid
     and False if It is not.
    :rtype: bool
    """
    try:
        supposed_phone = phonenumbers.parse(supposed_phone)
        return phonenumbers.is_valid_number(supposed_phone)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False
