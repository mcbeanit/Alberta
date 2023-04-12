import scrapy
import re


class ABPartiesSpider(scrapy.Spider):
    name = 'abpartiesspider'

    pattern = '^<li class="accordion-navigation".+?>(.+?)<\/a><div class="content".+?<div.+?<\/p><\/div><div.+?<p>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br><a href="(.+?)">(.+?)<\/a>.+<\/div><\/div><\/li>$'

    def start_requests(self):
        urls = {'https://www.elections.ab.ca/political-participants/parties/'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        p = response.css('li[class="accordion-navigation"]').getall()
        with open('ab_parties.csv', 'wt') as f:
            for party in p:
                self.parse_party(party, f)
                f.flush()
            f.close()

    def parse_party(self, html: str, f):
        html = str(html.replace("\n", ""))
        html = str(html.replace("\r", ""))
        matches = re.match(self.pattern, html)
        if matches is not None:
            f.write(str(matches[1]))
            f.write('\t')
            f.write(str(matches[2]))
            f.write('\t')
            f.write(str(matches[3]))
            f.write('\t')
            f.write(str(matches[4]))
            f.write('\t')
            f.write(str(matches[5]))
            f.write('\t')
            city = str(matches[6])
            city = city.replace("\xef\xbf\xbd", " ")
            f.write(city)
            f.write('\t')
            f.write('\n')
        else:
            self.log('The pattern was not matched')
            self.log(self.pattern)
            self.log(html)