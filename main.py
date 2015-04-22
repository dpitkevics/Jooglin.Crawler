from core.engine import Crawler

from pipelines import FilterPipeline, PrintPipeline
from downloaders import RequestsDownloader
from crawlers import ChildCrawler


if __name__ == '__main__':
    crawler = Crawler(
        downloader=RequestsDownloader(),
        pipelines=(FilterPipeline(), PrintPipeline())
    )

    crawler.crawl(ChildCrawler())