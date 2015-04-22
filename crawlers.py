from bs4 import BeautifulSoup
import requests
from requests.exceptions import MissingSchema, InvalidSchema, RequestException

from core.base import BaseCrawler

from httplib import ReqRequest


class ChildCrawler(BaseCrawler):
    ENTRY_REQUESTS = ReqRequest('http://jooglin.com')

    def extract_items(self, response):
        matches = []
        try:
            html_code = response.content.decode('utf8')

            soup = BeautifulSoup(html_code)
            for link in soup.find_all('a'):
                try:
                    requests.get(link)
                    matches.append(link.get('href'))
                except MissingSchema:
                    scheme = self.ENTRY_REQUESTS.scheme
                    hostname = self.ENTRY_REQUESTS.hostname

                    href = link.get('href')
                    if href.startswith('/'):
                        url_pattern = "%s://%s%s"
                    else:
                        url_pattern = "%s://%s/%s"
                    url = url_pattern % (scheme, hostname, href)
                    matches.append(url)
                except InvalidSchema:
                    pass
        except UnicodeDecodeError:
            pass

        return matches

    def next_requests(self, response):
        return [
            ReqRequest('http://facebook.com')
        ]