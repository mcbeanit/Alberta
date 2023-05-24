import scrapy
import re

class APCandidatesSpider(scrapy.Spider):
    name = 'abcandidatesspider'
    html_file = 'ap_candidates.html'

    def start_requests(self):
        urls = {'https://www.albertaparty.ca/candidates'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):
        html = response.css('div[class="col-md-3 facts-mb"]').getall()
        assert html
        assert len(html) > 0
        count = 0
        with open(self.html_file, 'wt') as f:
            for candidate in html:
                candidate = candidate.replace('\n', '')
                candidate = candidate.replace('\r', '')
                candidate = candidate.replace('\t', '')
                candidate = self.clean_html(candidate)
                count = count + 1
                if len(candidate) > 0:
                    f.write(f'{candidate}\n');
        f.close()
        print(f'ap_candidates_spider.py: found {count} candidates')

    def on_error(self, failure):
        pass

    def clean_html(self, div:str):
        div = re.sub('class=".+?"', "", div)
        div = div.replace(' For ', ' for ')  # for some matching that's case sensitive.
        div = div.replace('data-aos-delay=""', '')
        div = div.replace('data-aos=""', '')
        div = div.replace('delay=""', '')
        div = div.replace('target="_blank"', '')
        div = div.replace('alt=""', '')
        div = div.replace('data-aos-delay="0"', '')
        div = re.sub('>\\s+?<', '><', div)
        div = re.sub('<div\\s+?>', '<div>', div)
        div = re.sub('\\s+?>', '>', div)
        div = div.strip()
        return div


