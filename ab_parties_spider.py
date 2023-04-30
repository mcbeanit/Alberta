import scrapy
import json
import re


class ABPartiesSpider(scrapy.Spider):
    name = 'abpartiesspider'

    # get pattern1 from the json file
    f = open('settings.json')
    settings = json.load(f)
    f.close()
    s = settings['settings']
    p = s[0]
    # pattern = p['pattern1']

    # pattern = '^<li class="accordion-navigation".+?>(.+?)<\/a><div class="content".+?<div.+?<\/p><\/div><div.+?<p>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br><a href="(.+?)">(.+?)<\/a>.+<\/div><\/div><\/li>$'

    def start_requests(self):
        urls = {'https://www.elections.ab.ca/political-participants/parties/'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):

        p = response.css('li[class="accordion-navigation"]').getall()
        with open('ab_parties.html', 'wt') as f:
            for party in p:
                self.parse_party(party, f)
                f.flush()
            f.close()

    def on_error(self, failure):
        pass

    def parse_party(self, html: str, f):

        html = str(html.replace("\n", ""))
        html = str(html.replace("\r", ""))
        html = str(html.replace('\t', ""))

        html = re.sub(' class=".+?"', "", html)
        html = re.sub(' id=".+?"', "", html)
        html = re.sub('^<li\\s*?><button\\s.+?>', '<li><button>', html)
        html = re.sub('width=".+?"', "", html)
        html = re.sub('height=".+?"', "", html)
        html = re.sub(r'(?is) srcset="(.+?)</p>', '</p>', html)
        html = html.replace('alt=""', "")
        html = html.replace('decoding="async"', "")
        html = html.replace('loading="lazy"', "")

        f.write(f"{html}\n")
        f.flush()