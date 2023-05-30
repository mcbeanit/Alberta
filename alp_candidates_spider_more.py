import scrapy
import re
import os
import time


class ALPCandidatesSpiderMore(scrapy.Spider):
    """
    Use the candidates url to navigate into more information about
    the candidate.  In this case, not much is there.
    See ndp_candidates_spider_more.py
    """
    name = 'alpcandidatesspidermore'
    csv_file = 'alp_candidates.csv'
    html_file = 'alp_candidates_more.html'
    csv_file_more = 'alp_candidates_more.csv'
    name_pattern = r'^(.+?)\s\|\s(.+?)\s\-'

    if os.path.exists(csv_file_more):
        os.remove(csv_file_more)
    if os.path.exists(html_file):
        os.remove(html_file)

    def start_requests(self):
        urls = self.get_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)
            time.sleep(2)

    def parse(self, response, **kwargs):
        name = ''
        riding = ''
        headshot = ''

        name_riding = response.css('title::text').get()

        assert name_riding

        # e.g. Jacob Stacey | Sherwood Park - Alberta Liberal Party
        matches = re.match(self.name_pattern, name_riding)
        # print(name_riding)
        # assert matches
        if matches is not None:
            name = matches[1]
            riding = matches[2]
        else:
            # try and alternate match
            matches = re.match(r'^(.+?)\s\|\s(.+?)$', name_riding)
            if matches is not None:
                name = matches[1]
                riding = matches[2]
            else:
                print(f'title was not matched: {name_riding}')
                assert False

        # print(f'Data: {name} <> {riding}\n')
        bio_html = response.xpath('//div[@class="col-lg-6"]').getall()
        # get the candidate name and riding to associate with the bio'
        # e.g. h1 class="entry-title mt-3 mb-1">Zarnab Zafar </h1><span> Calgary-Beddington</span>
        # name_riding = ''
        # name_riding = response.xpath('//h1[@class="entry-title mt-3 mb-1"]/span')
        # if name_riding is not None:
        # name_riding = name_riding.replace('\n', '')
        # name_riding = name_riding.replace('\r', '')
        # name_riding = name_riding.replace('\t', '')

        bio = ''
        if bio_html is not None:
            if len(bio_html) == 0:
                print('This bio was not found')
            for bio_line in bio_html:
                bio_line = bio_line.replace('\n', '')
                bio_line = bio_line.replace('\r', '')
                bio_line = bio_line.replace('\t', '')
                bio_line = bio_line.strip()
                bio_line = bio_line.strip(u'\u200b')
                bio_line = re.sub(u'\u200b', '', bio_line)

                # bio = bio + bio_line
            with open(self.html_file, 'at') as f:  # will have to append here
                # f.write(f'ALP\t{name}\t{riding}\t{bio}\t{headshot}\n')
                f.write(f'{name}\t{riding}\t{bio_line}\n')
                f.flush()
            f.close()
        else:
            print('there is no bio here')
            assert False

    def on_error(self, failure):
        pass

    def get_urls(self):
        urls = []

        with open(self.csv_file, 'rt') as csv:
            for c in csv.readlines():
                cols = c.split('\t')
                url = f'https://www.albertaliberal.com/{cols[3]}'
                urls.append(url)
            csv.close()

        return urls
