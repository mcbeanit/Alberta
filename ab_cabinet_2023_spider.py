import scrapy
import re

class ABCabinet2023Spider(scrapy.Spider):
    name = 'ABCabinet2023Spider'

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/Executive_Council_of_Alberta'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pass



