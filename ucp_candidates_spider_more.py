import scrapy
import os
import time
import csv
import gender_guesser


class UCPCandidateSpiderMore(scrapy.Spider):
    name = 'ucpcandidatesspidermore'
    csv_file = 'ucp_candidates.csv'
    csv_more_file = 'ucp_candidates_more.csv'

    if os.path.exists(csv_more_file):
        os.remove(csv_more_file)

    def start_requests(self):
        urls = self.get_candidate_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)
            time.sleep(2)

    def parse(self, response, **kwargs):
        name: str = response.css('h1::text').get()
        riding: str = response.css('span[class="elementor-button-text"]::text').get()
        gender: str = ''
        if riding.startswith('AIrdrie'):
            riding = 'Airdrie-Cochrane'
        bio: str = ''
        paragraphs = response.xpath('//div[@class="elementor-widget-container"]/p/text()').getall()
        for p in paragraphs:
            p = p.replace('\n', '')
            p = p.replace('\r', '')
            p = p.replace('\t', '')
            bio = bio + p
            gender = gender_guesser.guess(bio)

        with open(self.csv_more_file, 'at') as f:
            f.write(f'UCP\t{name}\t{riding}\t{gender}\t{bio}\n')
            f.close()

    def on_error(self, failure):
        pass

    def get_candidate_urls(self):
        urls = []
        file = open(self.csv_file, newline='')
        reader = csv.reader(file, delimiter='\t')
        data = [row for row in reader]
        assert data
        count = 0

        for row in data:
            count = count + 1
            url = str(row[3])
            urls.append(url)

        return urls
