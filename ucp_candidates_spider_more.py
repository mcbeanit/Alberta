import scrapy
import os
import time
import csv
import gender_guesser
import re

class UCPCandidateSpiderMore(scrapy.Spider):
    name = 'ucpcandidatesspidermore'
    csv_file = 'ucp_candidates.csv'
    csv_more_file = 'ucp_candidates_more.csv'
    csv_social_file = 'ucp_candidates_social.csv'
    social_exp = r'^.+?href=\"((https|http)://.+?)\"'


    def start_requests(self):

        if os.path.exists(self.csv_more_file):
            os.remove(self.csv_more_file)
        if os.path.exists(self.csv_social_file):
            os.remove(self.csv_social_file)

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
            p = p.replace('\ufb01', '')
            bio = bio + p
            gender = gender_guesser.guess(bio)

        with open(self.csv_more_file, 'at') as f:
            f.write(f'UCP\t{name}\t{riding}\t{gender}\t{bio}\n')
            f.close()

        # try to extract social media links. not all candidates have them
        # generally only; twitter, facebook, instagram, candidates website
        social = response.xpath('//a[@class="jet-listing-dynamic-link__link"]').getall()
        if social is not None:
            for a in social:
                # print(f'link: {a}\n')
                matches = re.match(self.social_exp, a)
                if matches is not None:
                    link = matches[1].strip()
                    platform = None
                    if 'facebook' in link:
                        platform = 'Facebook'
                    if 'instagram' in link:
                        platform = 'Instagram'
                    if 'twitter' in link:
                        platform = 'Twitter'
                    if 'tiktok' in link:
                        platform = 'TikTok'
                    if platform is not None:
                        with open(self.csv_social_file, 'at') as f:
                            f.write(f'UCP\t{name}\t{riding}\t{platform}\t{link}\n')
                            f.close()

        else:
            print(f'No social links for: {name}\n')

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
