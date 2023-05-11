import scrapy
import re
import time
import os
import gender_guesser


class ABNDPCandidatesSpiderMore(scrapy.Spider):
    """
    Read the csv file of candidates and load the links into the candidate's bio
    and extract some more info using Scrapy to visit each candidates site.
    candidate sites named with the candidates name, 
    for example https://nagwanalguneid.albertandp.ca
    :return: None
    """
    name = 'abndbcandidatesspidermore'
    csv_file = 'ndp_candidates.csv'
    html_file = 'ndp_candidates_more.html'
    csv_file_more = 'ndp_candidates_more.csv'
    html_social = 'ndp_candidates_social.html'

    if os.path.exists(csv_file_more):
        os.remove(csv_file_more)
    if os.path.exists(html_file):
        os.remove(html_file)
    if os.path.exists(html_social):
        os.remove(html_social)

    def start_requests(self):
        """
        get each candidates web address and let scrapy retrieve each one and
        save to temp html files.
        :return: None
        """
        urls = self.get_urls()
        # print(urls)
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)
            time.sleep(3)

    def parse(self, response):
        bio_html = response.css('div[class="about-person-holder"]').getall()
        candidate_name = response.css('h1[class="hero-fullname"]::text').get()
        riding = response.css('h2[class="hero-ridingname"]::text').get()
        social = response.xpath('//ul[@class="follow-links"]/li').getall()
        # assert social
        gender = ''
        about = response.xpath('//div[@class="about-bio abndp-home2022/text-style"]/p').getall()
        bio = ''

        for p in about:
            s = str(p)
            s = str(s.replace('\r', ''))
            s = str(s.replace('\n', ''))
            s = str(s.replace('\t', ''))
            s = str(s.replace('<p>', ''))
            s = re.sub('</p>', '', s)
            s = s.replace('<br>', '')
            bio = bio + s
            gender = gender_guesser.guess(bio)

        assert (bio is not None)
        assert (candidate_name is not None)
        assert (riding is not None)
        assert (bio_html is not None)
        with open(self.csv_file_more, 'at') as f:  # will have to append here
            f.write(f'{candidate_name}\t{riding}\t{gender}\t{bio}\n')
            f.close()

        if social is not None:
            with open(self.html_social, 'at') as f:
                for l in social:
                    l = l.replace('\n', '')
                    l = l.replace('\r', '')
                    l = l.replace('\t', '')
                    f.write(f'{candidate_name}\t{riding}\t{l}\n')
                f.close()
        else:
            print(f'{candidate_name}: No social links found.\n')

    def on_error(self, failure):
        """
        report and errors the crawler encountered that caused an error event.
        :param failure: error information
        :return: None
        """
        with open('error.log', 'a') as err:
            err.write(f'{self.name},{failure}\n')

    def get_urls(self):
        """
        build a list of the candidates urls.
        :return: list of urls
        """
        urls = []

        with open(self.csv_file, 'rt') as csv:
            for c in csv.readlines():
                cols = c.split('\t')
                url = f'https:{cols[3]}'
                urls.append(url)
            csv.close()

        return urls
