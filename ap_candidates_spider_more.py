import scrapy
import re
import os
import csv
import time


class APCamdidatesSpiderMore(scrapy.Spider):
    """
      Use the candidates url to navigate into more information about
      the candidate.  In this case, not much is there.
      See ndp_candidates_spider_more.py
      """
    name = 'apcandidatesspidermore'
    csv_file = 'ap_candidates.csv'
    html_file = 'ap_candidates_more.html'
    csv_file_more = 'ap_candidates_more.csv'
    name_pattern = r'^(.+?)\s[Ff]or\s(.+?)$'
    short_name = 'AP'
    candidate_domain = 'https://www.albertaparty.ca'

    if os.path.exists(csv_file_more):
        os.remove(csv_file_more)
    if os.path.exists(html_file):
        os.remove(html_file)

    def start_requests(self):
        urls = self.get_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)
            time.sleep(3)

    def parse(self, response, **kwargs):
        name_riding = ''
        name = ''
        riding = ''
        canonical_url = ''

        name_riding = response.css('title::text').get()
        assert name_riding
        # print(f'Name: {name_riding}\n')

        matches = re.match(self.name_pattern, name_riding)
        if matches is not None:
            name = matches[1]
            riding = matches[2]
        else:
            # print('title was not matched')
            assert False

        # there are multiple divs tagged the same way so we have to get all of them
        # and find the one that has the bio text.  they don't have any id attribute that
        # can distinguish them. also the html is broken in place
        # we probably want the first one, but this has to be tested.
        # also getting the social media links in this section(new)

        divs = response.css('div[class="row"]').getall()
        assert divs
        div_bio = divs[0]
        assert len(div_bio) > 0
        div_bio = div_bio.replace('\n', '')
        div_bio = div_bio.replace('\r', '')
        div_bio = div_bio.replace('\t', '')

        with open(self.html_file, 'at') as f:
            f.write(f'{self.short_name}\t{name}\t{riding}\t{div_bio}\n')
            f.flush()
        f.close()

    def on_error(self, failure):
        print(failure)

    def get_urls(self):
        urls = []

        file = open(self.csv_file, newline='')
        reader = csv.reader(file, delimiter='\t')
        data = [row for row in reader]
        assert data

        for u in data:
            url = str(u[3]).strip()
            if len(url) > 0:
                if url.startswith(self.candidate_domain):
                    urls.append(url)

        return urls
