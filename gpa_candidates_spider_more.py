import scrapy
import re
import csv
import time
import os

class GPACandidatesSpideMore(scrapy.Spider):
    name = 'gpacandidatesspidermore'
    csv_file = 'gpa_candidates.csv'
    html_file = 'gpa_candidates_spider_more.html'
    html_social = 'gpa_candidates_social.html'
    name_pattern = r'^(.+?)\s[Ff]or\s(.+?)$'
    short_name = 'GPA'


    def start_requests(self):

        if os.path.exists(self.html_file):
            os.remove(self.html_file)
        if os.path.exists(self.html_social):
            os.remove(self.html_social)

        urls = self.get_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)
            time.sleep(3)

    def parse(self, response, **kwargs):
        name = ''
        riding = ''
        name_riding = response.css('title::text').get()
        assert name_riding
        matches = re.match(self.name_pattern, name_riding)
        if matches is not None:
            name = matches[1]
            riding = matches[2]
        else:
            assert False

        social = response.xpath('//div[@class="col"]/p/a').getall()
        assert social

        with open(self.html_social, 'at') as social_file:
            for a in social:
                a = a.replace('\n', '')
                a = a.replace('\r', '')
                a = a.replace('\t', '')
                social_file.write(f'{self.short_name}\t{name}\t{riding}\t{a}\n')
            social_file.close()

        bio_html = response.xpath('//div[@class="text-content"]/p').getall()
        assert bio_html
        with open(self.html_file, 'at') as bio_file:
            bio = ''
            for p in bio_html:
                p = p.replace('\n', '')
                p = p.replace('\r', '')
                p = p.replace('\t', '')
                p = p.replace(u'\xa0', '')
                bio = bio + ' ' + p
            bio_file.write(f'{self.short_name}\t{name}\t{riding}\t{bio}\n')
            bio_file.close()


    def on_error(self, failure):
        pass

    def get_urls(self):
        urls = []
        file = open(self.csv_file, newline='')
        reader = csv.reader(file, delimiter='\t')
        data = [row for row in reader]
        assert data

        for row in data:
            url = row[3]
            urls.append(url)

        return urls


