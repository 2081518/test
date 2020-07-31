from urllib.parse import urlparse
import phonenumbers
import re


def validate_url_incomplete(url: str) -> bool:
    pattern = r"http[s]?:\/\/(?:www\.)?([\w]+)\."
    if len(re.findall(pattern, url)) > 0:
        return False
    else:
        return True


def validate_web_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def validate_image(supposed_image: str) -> bool:
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
    try:
        supposed_phone = phonenumbers.parse(supposed_phone)
        return phonenumbers.is_valid_number(supposed_phone)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False
