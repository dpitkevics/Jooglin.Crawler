import requests as requestslib

from core.base import BaseDownloader, BaseDownloadException

from core.utils import iterator

from httplib import ReqResponse


class RequestsDownloader(BaseDownloader):
    def get(self, requests):
        responses = []
        for request in iterator(requests):
            response = self._fetch(request)
            responses.append(response)
        return responses

    def _fetch(self, request):
        try:
            res = requestslib.get(request.url)
            return ReqResponse(request, res)
        except Exception as e:
            print('Exception on %s: %s', request, e)
            return BaseDownloadException(request, exception=e)