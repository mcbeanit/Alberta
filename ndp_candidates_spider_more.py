import scrapy
import re
import csv

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
            break


    def parse(self, response):
        bio = response.css('div[class="about-person-holder"]').getall()
        # should be only 1 section


        for b in bio:
            print(b)


    def on_error(self, failure):
        """
        report and errors the crawler encountered that caused an error event.
        :param failure: error information
        :return: None
        """
        pass

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

        return urls






if __name__ == '__main__':
    parse_candidates_more()
