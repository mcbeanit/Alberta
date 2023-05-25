import scrapy

import ab_338_ridings


class AB338Spider(scrapy.Spider):
    name = 'ab338spider'

    def start_requests(self):
        urls = {'https://338canada.com/alberta/districts.htm'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response, **kwargs):
        trs = response.xpath('//table[@id="myTable"]/tr').getall()
        with open('ab_338_ridings.html','wt') as html:
            count = 0
            # ignore the first line which is a row header
            for tr in trs:
                count = count + 1
                if count > 1:
                    tr = tr.replace('\n', '')
                    tr = tr.replace('\r', '')
                    tr = tr.replace('\t', '')
                    html.write(f'{tr}\n')

        html.close()
        print (f'ab_338_spider.py: found {count} ridings, expected 87')



    def on_error(self, failure):
        print(failure)
        assert False
