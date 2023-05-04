import scrapy
import re

public class OfficialCandidatesSpider(scrapy.Spider):
    name = officialcandidatesspider

    def start_requests(self):
        url = {'https://www.elections.ab.ca/current-election-information/candidates/'}
        yield scrapy.Request(url=url, allback=self.parse, errback=self.on_error)

    def parse(self, response):
        pass

    def on_error(self, failure):
        pass

    


