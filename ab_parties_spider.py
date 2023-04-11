import scrapy
import re

pattern = '^<li class=.+?><a href=.+?><p>(.+)<\/p><\/div>.+<p>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br><a href=(' \
          '.*)<\/a>.*<\/li>$'

class ABPartiesSpider(scrapy.Spider):
    name = 'abpartiesspider'


    def start_requests(self):
        urls = {'https://www.elections.ab.ca/political-participants/parties/'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        p = response.css('li[class="accordion-navigation"]').getall()
        with open('test.html', 'wt') as f:
            for party in p:
                f.write(f"{party}\n\n\n")
                f.flush()
            f.close()
