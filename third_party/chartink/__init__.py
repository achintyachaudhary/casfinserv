import ssl

import requests
from bs4 import BeautifulSoup

from third_party.chartink.config import CHARTINK_BASE_URL


class ChartInk:
    csrf_token = ""

    def __init__(self):
        def parse_csrf_token():
            response = requests.request("GET", CHARTINK_BASE_URL)
            # Create a BeautifulSoup object
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all meta tags
            meta_tags = soup.find_all('meta')
            # Iterate over the meta tags
            for meta in meta_tags:
                tag_name = meta.get('name')
                tag_content = meta.get('content')
                if tag_name == 'csrf-token':
                    return tag_content, self.get_parsed_cookie(response.headers['set-cookie'])

        self.csrf_token, self.cookie = parse_csrf_token()

    def get_parsed_cookie(self, cookie):
        cookie = cookie.split(";")
        cookie = cookie[0] + ";" + cookie[3].split(",")[1]
        return cookie
