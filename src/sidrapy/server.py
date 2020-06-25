
"""
This module abstract a server object
It contains actions that interact directly with IBGE Api's servers
"""


import time
import urllib.parse

import requests


ADDRESS = 'api.sidra.ibge.gov.br'


class ConnectionError(Exception):
    pass


def create_url(path: str):
    """Creates api url"""

    info = dict(
        schema='http',
        netloc=ADDRESS,
        path=path,
        params='',
        query='',
        fragment='',
    )
    url = urllib.parse.urlunparse(info.values())
    return url



def ping():
    """
    Http get main address and returns the response time in miliseconds
    Note: this is not a true ping with ICMP protocol
    """
    
    url = create_url('/')
    start = time.time()
    r = requests.get(url, timeout=10)
    end = time.time()
    if r.status_code != 200:
        msg = 'Expected status code 200 but got ' + str(r.status_code)
        raise ConnectionError(msg)
    return (end - start) * 1000
