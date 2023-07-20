import scrapy
import re

class ABCabinet2023Spider(scrapy.Spider):
    name = 'ABCabinet2023Spider'
    html_file = 'ab_cabinet_2023.html'


    def start_requests(self):
        url = 'https://en.wikipedia.org/wiki/Executive_Council_of_Alberta'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        trs = response.xpath('//table[@class="wikitable"]/tbody/tr').getall()
        with open (self.html_file, 'wt') as html:
            count = 0
            # ignore the first line which is a row header
            # print (trs)
            for tr in trs:
                count = count + 1
                if count > 1:
                    tr = tr.replace('\n', '')
                    tr = tr.replace('\r', '')
                    tr = tr.replace('\t', '')
                    html.write(f'{tr}\n')
        html.close()



