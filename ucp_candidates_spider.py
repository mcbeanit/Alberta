import scrapy
import re

class UCPCandidatesSpider(scrapy.Spider):
    name = 'ucpcandidatesspider'

    def start_requests(self):
        # urls = {'https://www.unitedconservative.ca/nominated-candidates/'}
        urls = {'file:///C:/Users/owner/PycharmProjects/alberta/Nominated Candidates–UCP.html'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        html = response.css('section').getall()
        with open('ucp_candidates.html', 'wt') as f:
            count = 0
            for c in html:
                count = count + 1
                # ignore the <section> tags that come before or after list of candidates with
                # section tags. may have to adjust these counts but probably not.  sections
                # for each candidate are sorted by riding name.  (airdrie->yellowhead)
                # there should be a full list of 87 now.
                if count < 3 or count > 80:
                    continue
                c = c.replace('\n',"")
                c = c.replace('\r',"")
                c = c.replace('\t',"")
                c = self.clean_html(c)
                f.write(f'{c}\n')
                f.flush()


        f.close()

    def clean_html(self, c):

        c = re.sub(' class=".+?"', " ", c)
        c = re.sub(' id=".+?"', " ", c)
        c = c.replace('data-id="90549ed"', "")
        c = c.replace('data-id="5a5c84a"', "")
        c = c.replace('data-id="53e3753"', "")
        c = c.replace('data-id="de87933"', "")
        c = c.replace('data-id="110b263"', "")
        c = c.replace('data-id="99b8aca"', "")
        c = c.replace('data-element_type="section"', "")
        c = c.replace('data-element_type="column"', "")
        c = c.replace('data-element_type="widget"', "")
        c = re.sub("data-settings='.+?'", "", c)
        c = c.replace('data-element_type="column"', "")
        c = c.replace('decoding="async"', "")
        c = re.sub('width="[0-9]+?"', "", c)
        c = re.sub('height="[0-9]+?"', "", c)
        c = c.replace('alt=""', "")
        c = c.replace('loading="lazy"', "")
        c = c.replace('data-widget_type="image.default"', "")
        c = c.replace('data-widget_type="text-editor.default"', "")
        c = c.replace('data-widget_type="button.default"', "")
        c = re.sub('srcset=".+?"', "", c)
        c = re.sub('sizes=".+?"', "", c)
        c = c.replace('role="button"', "")

        # should be no attributes, or tags not needed. get rid of dead space in opening tags
        c = re.sub('<section\\s+?>', '<section>', c)
        c = re.sub('<div\\s+?>', '<div>', c)
        c = re.sub('<span\\s+?>', '<span>', c)

        # dead space between nodes
        c = re.sub('<section>\\s+?<div>', '<section><div>', c)
        c = re.sub('<div>\\s+?<div>', '<div><div>', c)
        c = re.sub('<div>\\s+?<div>', '<div><div>', c)
        c = re.sub('<div>\\s+?<div>', '<div><div>', c)
        c = re.sub('<div>\\s+?<img', '<div><img', c)
        c = re.sub('<img\\s+?src=', '<img src=', c)
        c = re.sub('png"\\s+?>', 'png">', c)
        c = re.sub('jpg"\\s+?>', 'jpg">', c)
        c = re.sub('jpeg"\\s+?>', 'jpeg">', c)
        # dead space inner htnl
        c = re.sub('>\\s+?<', '><', c)

        c = c.replace('</div></div></div><div><div><div', '</div><div')

        # redundant span tags with no data
        c = c.replace('<span><span>Read</span></span>','')
        # repeating div that have no data
        c = c.replace('<section><div><div><div><div><div><div><div><div>', '<section>')
        # empty closing tags or weird spaces after url
        c = c.replace('</a></div></div></div></div></div></div></div></div></section>', '</a></div></section>')
        c = c.replace('"  ></a>', '"></a>')
        # typos
        c = c.replace('AIrdrie', 'Airdrie')


        """
        
        c = c.replace('elementor-section '," ")
        c = c.replace('elementor-top-section '," ")
        c = c.replace('elementor-element '," ")
        c = c.replace('elementor-element-'," ")
        c = c.replace('elementor-section-boxed'," ")

        c = c.replace('elementor-section-height-default'," ")
        
        c = c.replace('data-element_type="widget"', "")
        
        c = c.replace('data-widget_type="nav-menu.default"',"")
       

        c = c.replace('data-elementor-type="jet-listing-items"',"")
        c = c.replace('data-widget_type="divider.default"',"")
       
        
        

        c = c.replace('sub-menu'," ")
        c = c.replace('elementor-nav-menu--dropdown'," ")
        c = re.sub('tabindex="[-?0-9]+?"'," ",c)
        c = c.replace('role="group"'," ")
        c = c.replace('aria-label="Menu Toggle"'," ")

        c = c.replace('aria-hidden="true"'," ")
        c = c.replace('aria-haspopup="true"'," ")
        c = c.replace('aria-current="page"'," ")
       
        c = c.replace('aria-expanded="false"'," ")
        
        
        c = re.sub('style=".+?"'," ",c)

        
        c = re.sub(' data-smartmenus-id=".+?"',"",c)
       
       
        c = re.sub('data-widget_type=".+?"'," ",c)

        c = re.sub("data-nav='{(.+?)}'"," ",c)
        c = c.replace('<li >','<li>')
        c = re.sub('aria-labelledby=".+?"'," ",c)
        c = re.sub('aria-controls=".+?"'," ",c)
        c = re.sub('data-elementor-id="[0-9].+?"'," ",c)

        
        c = c.replace('role="presentation"',"")
        c = c.replace('style=""'," ")
        c = c.replace('<li  >','<li>')
        c = re.sub('<a\\s+?','<a ',c)

        c = re.sub('<ul\\s+?>','<ul>',c)
       
        c = re.sub('<i\\s+?>',"<i>",c)
        c = re.sub('<div\\s+?>',"<div>",c)
        c = re.sub('>\\s+?<', "><", c)

        c = re.sub('<h2\\s+?>',"<h2>",c)
        c = c.replace('<div>				','>')
        
        c = c.replace('					<','<')
        c = c.replace('<img     ','<img ')
        c = c.replace('img   src', 'img src')
      
        c = c.replace('"    >', '">')
        
        """

        return c

