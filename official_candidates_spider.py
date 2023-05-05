import scrapy
import re


class OfficialCandidatesSpider(scrapy.Spider):
    name = 'officialcandidatesspider'
    exp_tbody = r'^^<table.+?<tbody>(.+)<\/tbody>'
    exp_fields = r'^<tr><td\s.+?>(.+?)<br>(.+?)<br>.+?<td\s.+?>(.+?)<br>.+<\/td><\/tr>$'
    # exp_rows = r'^<table.+?(<tr>(.*?><td.+?<\/td>)<\/tr>)+'
    # exp_riding = r'^<div.+?id=\"(.+?)\">'  if we need to get the riding id

    def start_requests(self):
        urls = {'https://www.elections.ab.ca/current-election-information/candidates/'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):
        # each riding is a <table>, and the candidates in that riding are <tr>
        table = response.xpath('//div[@class="content"]/table[@class="has-alt-colors"]').getall()
        assert table
        with open('official_candidates.html', 'wt') as data:
            for c in table:
                if c.__contains__('id="all-candidates"'):
                    continue
                c = c.replace('\n', '')
                c = c.replace('\r', '')
                c = c.replace('\t', '')
                data.write(f'{c}\n')
                matches = re.match(self.exp_tbody, c)
                if matches is not None:
                    body = matches[1]
                    body = re.sub('</tr>', '</tr>\n', body)
                    body = body.strip().split('\n')
                    count = 0
                    for b in body:
                        count = count + 1
                        matched = re.match(self.exp_fields, b)
                        if matched is not None:
                            pass # data.write(f'{matched[1].title()}\t{matched[2].title()}\t{matched[3].title()}\n')
                else:
                    data.write(f'not matched({body})\n')
                    assert False

            data.close()

    def on_error(self, failure):
        pass
