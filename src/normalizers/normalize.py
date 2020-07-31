import phonenumbers


def normalize_phone_number_list(phone_list: list) -> list:
    phone_list = list(filter(None.__ne__, phone_list))
    phone_list = list(filter(' '.__ne__, phone_list))
    phone_list = list(filter(''.__ne__, phone_list))
    return phone_list


def normalize_phone_number(number: str):
    try:
        number = phonenumbers.parse(number)
        return phonenumbers.format_number(number, 1)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None


def normalize_url(host: str, url: str) -> str:
    return host + url
