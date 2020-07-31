from src.validations.validate import validate_image, validate_web_url, validate_url_incomplete
from src.normalizers.normalize import normalize_url
import re


def extract_website_logo(host: str, tree) -> str:
    logo_xpaths = [
        '//*[contains(@{attribute}, "{attribute_name}")]/@{result}',
    ]
    attribute_names = [
        'img',
        'Img',
        'image',
        'Image',
        'ico',
        'Ico',
        'icon',
        'Icon',
        'logo',
        'Logo'
    ]
    attributes = [
        'alt',
        'class',
        'id',
        'rel',
        'img',
        'meta'
    ]
    results = [
        'img',
        'content',
        'href',
        'src',
        'data'
    ]
    for logo_xpath in logo_xpaths:
        for attribute in attributes:
            for attribute_name in attribute_names:
                for result in results:
                    logo_xpath_named = logo_xpath.format(
                        attribute=attribute,
                        attribute_name=attribute_name,
                        result=result
                    )
                    logos = tree.xpath(logo_xpath_named)
                    for logo in logos:
                        if validate_url_incomplete(logo):
                            logo = normalize_url(host=host, url=logo)
                        if validate_web_url(logo):
                            if logo and validate_image(logo):
                                return logo
                        else:
                            pass


def extract_phone_number(body) -> list:
    phones = re.findall(r'([\d()+\- ]{8,})\b.*', body)
    return phones
