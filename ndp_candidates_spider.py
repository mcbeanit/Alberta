import scrapy
import json
import re

class ABNDPCandidatesSpider(scrapy.Spider):
    name = 'abndbcandidatesspider'

    def start_requests(self):
        urls = {'https://www.albertandp.ca/candidates'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.on_error)

    # we want to find all the <div class="candidate-list-item">
    def parse(self, response):
        count = 0
        html = response.css('div[class="candidate-list-item"]').getall()
        with open('ndp_candidates.html', 'wt') as f:
            for c in html:
                c = self.clean_html(c)
                f.write(c);
                f.write('\n')
                count = count + 1
        f.close()
        print (f'NDP: Crawler found {count} candidates')

    def on_error(self, failure):
        pass


    def clean_html(self, h):
        h = str(h.replace('\n',""))
        h = str(h.replace('\r',""))
        h = str(h.replace(' class="candidate-list-item"',""))
        h = str(h.replace('>		        <',"><"))
        h = str(h.replace(' class="block--candidates--item"',""))
        h = str(h.replace('>		  <','><'))
        h = str(h.replace(' class="item-inner"',""))
        h = str(h.replace('>		    		    <','><'))
        h = str(h.replace(' class="item-headshot"',""))
        h = str(h.replace('>		      <',"><"))
        h = str(h.replace(' class="item-headshot-img"',""))
        h = str(h.replace('>		    <', "><"))
        h = str(h.replace(' class="item-fullname"',""))
        h = str(h.replace(' class="item-ridingname"', ""))
        h = str(h.replace(' class="item-website-link"',""))
        h = str(h.replace(' target="_blank"', ""))
        h = str(h.replace(' class="website-link-text"', ""))
        h = str(h.replace('		              ', ""))
        h = str(h.replace('		            		  ', ""))
        h = str(h.replace('		</div>      </div>', '</div></div>'))
        h = str(h.replace(' class="item-tags-container"', ""))
        h = str(h.replace('    ', ""))
        h = str(h.replace(' class="item-tag"',""))
        h = str(h.replace('>				  <', "><"))


        return h