import scrapy
import re
import json

class ALPCandidatesSpider(scrapy.Spider):
    """
    Use scrapy to visit the Alberta Liberal Party candidates page and extract
    the relevant html to build a candidates list. (alp_candidates.csv)
    See also:  alp_candidates.py, alp_candidates_spider_more.py
    """
    name = 'alpcandidatesspider'

    def start_requests(self):
        urls = {'https://www.albertaliberal.com/candidates'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response, **kwargs):
        assert(response is not None)
        html = response.xpath('//div[@class="dropdown-menu"]/a').getall()
        count = 0
        with open('alp_candidates.html', 'wt') as h:
            for a in html:
                # note that the first line selected is not a candidate, but a header
                # and should be ignored.
                if a.__contains__('>Candidates<'):
                    continue
                count = count + 1
                a = a.replace('\\n', '')
                a = a.replace('\\r', '')
                a = a.replace('\\t', '')
                h.write(f'{a}\n')
            h.close()
        print(f'alp_candidates_spider.py: There were {count} candidates found')

    def on_error(self, failure):
        pass