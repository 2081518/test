from src.normalizers.normalize import normalize_phone_number, normalize_phone_number_list
from src.extractors.extract import extract_phone_number, extract_website_logo
from src.validations.validate import validate_phone

from io import StringIO
from lxml import etree
from sys import stdout
import json


def get_website_logo(host: str, body) -> str:
    """
    It'll receive a host and an HTML,
    process the HTML, and return the
    URL of the logo formatted.
    :param host: The host of the respective body
    :type host: str
    :param body: The HTML of some page
    :return: A URL of the website Logo
    :rtype: str
    """
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(body), parser=parser)
    photo = extract_website_logo(host=host, tree=tree)
    return photo


def get_phone_number(body) -> list:
    """
    It'll try to get all the phone numbers from the
    HTML and return a list containing the numbers.
    :param body: Some HTML
    :return: A lista of phone numbers encountered
    :rtype: list
    """
    phone_list = extract_phone_number(body=body)
    phones = [
        normalize_phone_number(number=phone.replace("\\", "").replace("/", ""))
        if validate_phone(phone) else None for phone in phone_list
    ]
    phones = normalize_phone_number_list(phones)
    return phones


def parse_result(result: tuple):
    """
    It'll cares of execute all the process
    of extracting the Logo URL and all
    phone numbers of some HTML and output
    It.
    :param result: The URL as the first index
     and the response as the second.
    :type result: tuple
    :return: The URL and the response of
     the page.
    :rtype: tuple
    """
    url = result[0]
    response = result[1]
    output = stdout
    if response == "DeadPage":
        output.write("DeadPage\n")
    else:
        body = response.content.decode("utf-8")
        logo = get_website_logo(host=url, body=body)
        phones = get_phone_number(body=body)
        data = {
            "phones": phones,
            "logo": logo,
            "website": url
        }
        output.write(json.dumps(data))
        output.write("\n")

    return url, response
