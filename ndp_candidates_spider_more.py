import scrapy
import re
import time
import os

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

    if os.path.exists(csv_file_more):
        os.remove(csv_file_more)
    if os.path.exists(html_file):
        os.remove(html_file)

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
            time.sleep(2)


    def parse(self, response):
        bio = response.css('div[class="about-person-holder"]').getall()
        name = response.css('h1[class="hero-fullname"]::text').get()
        riding = response.css('h2[class="hero-ridingname"]::text').get()
        print(f'Name: {name} - {riding}\n')
        about = response.xpath('//div[@class="about-bio abndp-home2022/text-style"]/p').getall();
        nice = ''
        # print(about)
        for p in about:
            s = str(p)
            s = str(s.replace('\\r', ''))
            s = str(s.replace('\\n', ''))

            s = s.replace('\t', '')
            s = s.replace('<p>', '')
            s = re.sub('<\\/p>', '', s)

            nice = nice + s

        assert(nice is not None)
        assert(name is not None)
        assert(riding is not None)
        assert(bio is not None)
        for b in bio:
            b = b.replace('\n', '')
            b = b.replace('\r', '')
            b = b.replace('\t', '')
            with open(self.csv_file_more, 'at') as f:  # will have to append here
                f.write(f'{name}\t{riding}\t{nice}\n')
                f.flush()
            f.close()


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
            csv.close()

        return urls

