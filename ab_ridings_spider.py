import scrapy
import re


class ABRidingsSpider(scrapy.Spider):
    name = 'abridingsspider'
    pattern = '^<tr><td>([0-9]+?)<\/td><td>(.+?)<\/td><td>([0-9\*]{4,5})<\/td><td>(.+?)<\/td><td bgcolor=\"(' \
              '.+?)\"><\/td><td>(.+?)<\/td><td>([0-9,]+?)<\/td>.*<\/tr>$'
    patternTitle = '^<a href="(.+?)"\s.*?title=".+?">(.+?)<\/a>$'
    patternMLA = '^<span data-sort-value=\"(.+?)\".*$'
    ridingCount = 87

    def start_requests(self):
        urls = {'https://en.wikipedia.org/wiki/List_of_Alberta_provincial_electoral_districts'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response)
        l = response.css('table').getall()
        filename = "ab_ridings.html"

        with open(filename, 'wt') as f:
            tbl: str = l[0]
            # try to take out random line feeds, and only place them after </tr>
            tbl = tbl.replace('\n', "")
            tbl = tbl.replace("</tr>", "</tr>\n")
            f.write(tbl)
            f.write("\n")
            f.flush()
        f.close()

        count: int = 0
        with open(filename, 'rt') as f:
            with open("alberta_ridings.csv", "wt") as w:
                for row in f:
                    if row.startswith('<tr>'):
                        count = count + 1
                        matches = re.match(self.pattern, row)
                        if matches is not None:
                            w.write(str(matches[1]))
                            w.write('\t')
                            matchesTitle = re.match(self.patternTitle, str(matches[2]))
                            if matchesTitle is not None:
                                w.write(str(matchesTitle[1]))
                                w.write('\t')
                                w.write(str(matchesTitle[2]))
                                w.write('\t')
                            w.write(str(matches[3]))
                            w.write('\t')
                            mla = str(matches[4])
                            matchesMLA = re.match(self.patternMLA, mla)

                            # mla name  (last, first)
                            w.write(str(matchesMLA[1]))
                            w.write('\t')

                            # party color is html hex
                            w.write(str(matches[5]))
                            w.write('\t')

                            # party name
                            w.write(str(matches[6]))
                            w.write('\t')

                            # population
                            w.write(str(matches[7]))

                            w.write('\n')

                        else:
                            w.write('Not matched: ', row)
            w.close()
        f.close()

        print(f'ab_ridings_spider.py: There were {count} ridings found')
        assert (count == self.ridingCount)
