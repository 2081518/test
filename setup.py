from setuptools import setup

setup(
    name='logo-photo-web-scraper',
    url='https://github.com/2081518/test',
    author='Thor Marinho',
    packages=[
        'src',
        'src.extractors',
        'src.initialization',
        'src.normalizers',
        'src.parsers',
        'src.scrapers',
        'src.validations'
    ],
    install_requires=[
        'certifi==2017.4.17',
        'cffi==1.13.2',
        'cryptography==2.8',
        'fake-useragent==0.1.7',
        'itsdangerous==0.24',
        'lxml==4.5.0',
        'parsel==1.2.0',
        'pyasn1==0.2.3',
        'pyasn1-modules==0.0.9',
        'PyDispatcher==2.0.5',
        'pyOpenSSL==17.5.0',
        'queuelib==1.4.2',
        'requests==2.13.0',
        'urllib3==1.22'
    ],
    version='0.1',
    license='2081518',
    description='A simple web scraper of logo and phone numbers',
    long_description=open('README.md').read()
)