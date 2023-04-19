import scrapy
import os
import json
import re


class UCPCandidatesSpider(scrapy.Spider):
    """
    The UCO does not have a formal candidate list yet, so this spider just gets the current MLS's
    and their details from their MLA list.  We need to delete those not running again, and add
    new candidates, and candidates running in opposition(ndp) ridings.
    """
    name = "ucpcandidatesspicder"
    csv_file = 'ucp_candidates.html'
    root_url = 'https://unitedconservativecaucus.ca'
    mla_count = 60
    count = 0

    def start_requests(self):

        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

        urls = \
            {
                'https://unitedconservativecaucus.ca/page/1/?post_type=post&cat_name=mlas&s',
                'https://unitedconservativecaucus.ca/page/2/?post_type=post&cat_name=mlas&s ',
                'https://unitedconservativecaucus.ca/page/3/?post_type=post&cat_name=mlas&s ',
                'https://unitedconservativecaucus.ca/page/4/?post_type=post&cat_name=mlas&s ',
                'https://unitedconservativecaucus.ca/page/5/?post_type=post&cat_name=mlas&s '
            }

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)



    def parse(self, response):

        html = response.css('article').getall()
        with open(self.csv_file, 'a') as f:
            for c in html:
                self.count = self.count + 1
                c = self.clean(c)
                f.write(c)
                f.write('\n')
                f.flush()
        f.close()

        print(f'There are {self.count} UCP MLAs listed here. (running total after each page)')


    def clean(self, c: str):
        c = c.replace('\n', "")
        c = c.replace('\r', "")
        c = c.replace('>														<','><')
        c = c.replace('>								<','><')
        c = c.replace('>									<','><')
        c = c.replace('href="https://unitedconservativecaucus.ca','href="')
        c = c.replace('src="https://unitedconservativecaucus.ca','src="')
        c = c.replace('>							<', '><')
        c = c.replace('>																<',"><")
        c = c.replace(' class="more"',"")
        c = c.replace('>						<','><')
        c = c.replace('>																								<','><')
        # brian jean riding name missing from website html -> Fort McMurray-Lac La Biche
        if str(c.__contains__('Brian Jean')):
            s = '>Brian Jean</a></h2><a href="/brian-jean/">'
            r = '>Brian Jean</a></h2><p>Fort McMurray-Lac La Biche</p><a href="/brian-jean/">'
            c = c.replace(s, r)

        return c

    def on_error(self, failure):
        pass
