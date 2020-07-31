from src.normalizers.normalize import normalize_phone_number, normalize_phone_number_list
from src.extractors.extract import extract_phone_number, extract_website_logo
from src.validations.validate import validate_phone

from io import StringIO
from lxml import etree
from sys import stdout
import json


def get_website_logo(host, body):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(body), parser=parser)
    photo = extract_website_logo(host=host, tree=tree)
    return photo


def get_phone_number(body) -> list:
    phone_list = extract_phone_number(body=body)
    phones = [
        normalize_phone_number(number=phone.replace("\\", "").replace("/", ""))
        if validate_phone(phone) else None for phone in phone_list
    ]
    phones = normalize_phone_number_list(phones)
    return phones


def parse_result(result):
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
