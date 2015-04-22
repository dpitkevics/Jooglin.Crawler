from urllib.parse import urlparse

from core.base import BaseHttpRequest, BaseHttpResponse


class ReqRequest(BaseHttpRequest):
    def __init__(self, url):
        self._url = url
        parsed_url = urlparse(self.url)

        self._scheme = parsed_url.scheme
        self._hostname = parsed_url.hostname

    @property
    def url(self):
        return self._url

    @property
    def scheme(self):
        return self._scheme

    @property
    def hostname(self):
        return self._hostname


class ReqResponse(BaseHttpResponse):
    def __init__(self, request, response):
        self.req = request
        self.resp = response

        if not isinstance(response, Exception):
            self.body = self.resp.text

    @property
    def request(self):
        return self.req

    @property
    def response(self):
        return self.resp

    @property
    def content(self):
        return self.response.content