import requests
from requests.exceptions import MissingSchema, InvalidSchema, RequestException

from core.base import BasePipeline


class FilterPipeline(BasePipeline):
    def process(self, crawler, item):
        try:
            response = requests.get(item)
            if response.status_code != 200:
                raise RequestException()
        except RequestException:
            return None

        return item


class PrintPipeline(BasePipeline):
    def process(self, crawler, item):
        print('Sentence: %s, length: %s' % (item, len(item)))
        return item