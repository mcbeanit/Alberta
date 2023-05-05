import scrapy
import re


class OfficialCandidatesSpider(scrapy.Spider):
    name = 'officialcandidatesspider'
    exp_tbody = r'^<table.+?<tbody>(.+>)<\/tbody>'
    exp_rows = r'^<table.+?(<tr>(.*?><td.+?<\/td>)<\/tr>)+'
    # exp_riding = r'^<div.+?id=\"(.+?)\">'  if we need to get the riding id

    def start_requests(self):
        urls = {'https://www.elections.ab.ca/current-election-information/candidates/'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):
        # each riding is a <table>, and the candidates in that riding are <tr>
        table = response.xpath('//div[@class="content"]/table[@class="has-alt-colors"]').getall()
        assert table
        riding = ''

        with open('official_candidates.html', 'wt') as data:
            for c in table:
                c = c.replace('\n', '')
                c = c.replace('\r', '')
                c = c.replace('\t', '')

                matches = re.match(self.exp_rows, c)
                if matches is not None:
                    data.write(f'{riding},{c}\n')
                else:
                    data.write('not matched\n')

            data.close()

    def on_error(self, failure):
        pass
