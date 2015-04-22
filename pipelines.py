import requests
from requests.exceptions import MissingSchema, InvalidSchema, RequestException

from core.base import BasePipeline


class FilterPipeline(BasePipeline):
    def process(self, crawler, item):
        try:
            response = requests.get(item)
            if response.status_code != 200:
                raise RequestException()
        except MissingSchema:
            scheme = crawler.ENTRY_REQUESTS.scheme
            hostname = crawler.ENTRY_REQUESTS.hostname
            url = "%s://%s%s" % (scheme, hostname, item)

            return self.process(crawler, url)
        except InvalidSchema:
            return None
        except RequestException:
            return None

        return item


class PrintPipeline(BasePipeline):
    def process(self, crawler, item):
        print('Sentence: %s, length: %s' % (item, len(item)))
        return item