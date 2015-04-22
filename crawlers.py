import re

from core.base import BaseCrawler

from httplib import ReqRequest


python_sentence_re = re.compile('''<a[^>]+href="([^>]+)">''')


class ChildCrawler(BaseCrawler):
    ENTRY_REQUESTS = ReqRequest('http://jooglin.com')

    def extract_items(self, response):
        try:
            html_code = response.content.decode('utf8')
            matches = python_sentence_re.findall(html_code)
        except UnicodeDecodeError as e:
            print(e)
            matches = tuple()

        return matches

    def next_requests(self, response):
        return [
            ReqRequest('http://facebook.com')
        ]
        return None