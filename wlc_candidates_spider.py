import scrapy


class WLCCandidatesSpider(scrapy.Spider):
    name = 'wlccandidatesspider'

    def start_requests(self):
        urls = {'https://wildroseloyaltycoalition.com/our-candidates/'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):
        content = response.css('article').getall()
        assert content
        with open('wlc_candidates.html', 'wt') as html:
            count = 0
            for c in content:
                count = count + 1
                if count > 1:
                    c = c.replace('\n', '')
                    c = c.replace('\r', '')
                    c = c.replace('\t', '')
                    html.write(f'{c}\n');
        html.close()
        print(f'wlc_candidates_spider.py: There were {count} candidates found.')

    def on_error(self, failure):
        pass
