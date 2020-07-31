# Scrape Logos and Phone Numbers, from Web Sites
This program uses most of built-in libraries of Python 3.5. It receive a list of URL's, validate them, makes a request for each one, get the responses and respectively, scrape their Logo links and all the phone numbers encountered in the web page HTML.

Here are three different ways of run It:

- Run with docker
    - If the docker wasn't builded yet, then:
        - Verify if you has no permission to execute, then:
            - `chmod u+x docker_build.sh`
            - `./docker_build.sh`
            - `cat <file.txt> | docker run -i scrape_logo_and_phone_number`
        - Else, then:
            - `./docker_build.sh`
            - `cat <file.txt> | docker run -i scrape_logo_and_phone_number`
   - Else, then:
        - `cat <file.txt> | docker run -i scrape_logo_and_phone_number`

- Run with Python 3
    - If you want to pass a file.txt with web sites, then:
        - `cat websites.txt | Python3 main.py`
    - Else, if you want to pass the web sites through the command line, then:
        - `Python3 main.py https://website.com, https://website1.com, https://website2.com`

- Run with Python3 -m
    - `pip install https://github.com/2081518/test`
    - `cat websites.txt | Python3 -m main.py`
