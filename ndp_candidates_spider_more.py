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
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)


    def parse(self, response):
        pass

    def on_error(self, failure):
        """
        report and errors the crawler encountered that caused an error event.
        :param failure: error information
        :return: None
        """
    def get_urls(self):
        """
        build a list of the candidates urls.
        :return: list of urls
        """
        urls = []

        with open(self.csv_file, 'wt') as csv:
            pass


        return urls







if __name__ == '__main__':
    parse_candidates_more()
