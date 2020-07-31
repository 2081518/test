import asyncio
import requests
import concurrent.futures

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def mk_request(url: str):
    """
    Function to make request with
    Get method and return the photo
    as a response.
    :param url: photo URL
    :type url: str
    :return photo
    :rtype Response
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = None
    try:
        response = requests.get(
            url=url,
            headers=headers,
            stream=True,
            verify=False
        )
    except:
        pass

    if response and response.status_code in [200, 201, 202, 300, 301, 302, 303, 304]:
        return url, response
    else:
        return url, "DeadPage"


def concurrent_function(function: callable, args: list, max_workers: int = 10) -> isinstance:
    """
    Make execution of function asynchronously.
    :param function: Function to run concurrently
    :type function: callable
    :param args: Arguments of the target function
    :type args: list
    :param max_workers: Maximum number of workers.
        PS.: If a number less than 1 is set, it
            will assume the value as None and
            will execute all the free threads.
    :type max_workers: int
    :return: Object with returns of the determined function called
    :rtype object
    """
    if max_workers < 1:
        max_workers = None

    async def main():
        results = list()
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    function,
                    arg
                )
                for arg in args
            ]
            for url, response in await asyncio.gather(*futures):
                results.append((url, response))

        return results

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(main())
