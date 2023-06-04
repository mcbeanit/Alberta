import scrapy
import re

"""
Summary of party standings from Elections Alberta website. 
May change slightly after recounts
"""


class AB2023PartyStandingsSpider(scrapy.Spider):
    name = 'ab2023partystandingsspider'

    def start_requests(self):
        url = 'file:///C:/Users/owner/Downloads/Unofficial Results - 2023 Provincial General Election.html'
        yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response, **kwargs):
        assert response
        with open('ab_2023_party_standings.html', 'wt') as h:
            # riding_html =response.css(f'tr[id="ward-{riding.zfill(2)}"]').get()
            riding_html = response.css(f'td[class="ward-widget-number"]').getall()
            for l in riding_html:
                l = l.replace('\n', '')
                l = l.replace('\r', '')
                l = l.replace('\t', '')
                l = re.sub(r'>\s+?<', '><', l)
                h.write(f'{l}\n')
        h.close()

    def on_error(self, error):
        assert false
