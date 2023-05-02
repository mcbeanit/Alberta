import scrapy
import json
import re

class APCandidatesSpider(scraoy.Spider):
    name = 'abcandidatesspider'
    html_file = 'ap_candidates.html'

    def start_request(self):
        urls = {'https://www.albertaparty.ca/candidates'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):
        html = response.css('some selector in the html').getall()
        with open(html_file, 'wt') as f:
            for candidate in html:
                candidate = candidate.replace('\\n', '')
                candidate = candidate.replace('\\r', '')
                candidate = candidate.replace('\\t', '')
                candidate = self.clean_html(candidte)
                f.write(f'{{c}\n');
                

    def on_error(self, failure):
        pass

    def clean_html(self, h):
        return h


