import re
import json

csv_file =  'ucp_candidates.csv'
html_file = 'ucp_candidates.html'
pattern = r'^<article><figure><a href=\"(.+?)\"><img src=\"(.+?)\"></a></figure><figcaption><h2>.+?>(.+?)</a></h2><p>(.+?)</p>'
count = 0
def parse_candidates_html():

    with open(html_file, 'rt') as html, open(csv_file, 'wt') as csv:
        global count
        for c in html.readlines():
            count = count + 1
            c = clean(c)
            candidate = parse_candidate(c)
            # print(candidate)


def parse_candidate(c: str):
    matches = re.match(pattern, c)
    if matches is not None:
        pass
    else:
        print ('The pattern was not matched: \n')
        print (f'{c}\n')


    return c


def clean(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
