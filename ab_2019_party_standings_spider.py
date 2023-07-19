import scrapy
import re


def on_error(error):
    print(error)
    assert False


def html_clean(tr):
    tr = re.sub(r'<tr .+?>', '<tr>', tr)
    tr = re.sub(r'<td.+?>', '<td>', tr)
    return tr


class AB2019PartyStandingsSpider(scrapy.Spider):
    name = 'AB2019PartyStandingsSpider'

    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/2019_Alberta_general_election'
        yield scrapy.Request(url=url, callback=self.parse, errback=on_error)

    def parse(self, response, **kwargs):
        tables = response.css('table.wikitable tr').getall()
        print(tables[0:15])
        with open('ab_2019_party_standings_spider.html', 'wt') as html:
            for tr in tables[7:21]:
                tr = tr.replace('\n', '')
                tr = tr.replace('\r', '')
                tr = tr.replace('\t', '')
                tr = re.sub('\u2003', '', tr)
                tr = re.sub('\u2212', '', tr)
                tr = html_clean(tr)
                html.write(f'{tr}\n')

