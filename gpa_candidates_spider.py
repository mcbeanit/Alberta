import scrapy
import re


class GPACandidatesSpider(scrapy.Spider):
    name = 'GPACandidatesSpider'
    expected_count = 41
    pattern = '(src=)'  # (https:..assets.+?png)'

    def start_requests(self):
        urls = {'https://www.greenpartyofalberta.ca/2023_candidates'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    def parse(self, response):
        # query -? div class="plank-container-inner">
        count = 0
        p = response.css('div[class="plank-container-inner"]').getall()
        with open('gpa_candidates.html', 'wt') as f:
            for c in p:
                count = count + 1
                c = c.replace('\n', "")
                c = c.replace('\r', "")
                c = c.replace('\t', "")
                c = c.replace("  ", " ")
                c = re.sub(f'>\\s+?<', '><', c)
                f.write(f'{c}\n')
                f.flush()
            f.close()

        print(f'gpa_candidates_spider.py: There were {count} candidates found. Expected {self.expected_count}')

    def on_error(self, failure):
        pass
