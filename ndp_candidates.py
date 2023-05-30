import re
import csv
import operator

"""
Read the ndp candidate list html (ndp_candidates.html) and turn it into
a csv file (tab-delimited).
"""

candidate_exp = r'^<div><div><article><div><img data-src=\"(.*?)\"></div><h1>(.+?)</h1><h2>(.+?)</h2><a href=\"(.+?)\"><span>(.+?)</span></a>'
def parse_candidates_html(htmlfile='ndp_candidates.html', csvfile='ndp_candidates.csv'):
    """
    Read the html from the NDP Candidate list and extract relevant
    fields into a csv file.
    :param htmlfile: The name of the input html file (default = ndp_candidates.html)
    :param csvfile:  The name of the output csv file (default = ndp_candidates.csv)
    :return: None
    """
    count = 0
    expected_count = 87
    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csvout:
        for c in html.readlines():
            count = count + 1
            c = clean_html(c)
            candidate = parse_candidate(c)
            csvout.write('NDP\t')
            csvout.write(f'{candidate[1]}\t')
            csvout.write(f'{candidate[2]}\t')
            csvout.write(f'{candidate[3]}\t')
            csvout.write(f'{candidate[0]}\t')
            csvout.write('\n')

    html.close()
    csvout.close()

    with open(csvfile, 'rt') as r:
        reader = csv.reader(r, delimiter='\t')
        list = sorted(reader, key=operator.itemgetter(2), reverse=False)

    # rewrite the sorted file
    with open(csvfile, 'wt') as s:
        for p in list:
            s.write(f'{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\n');

    print(f'ndp_candidates.py: There are {count} candidates and {expected_count} expected. \n')


def parse_candidate(c: str):
    headshot: str = ''
    name: str = ''
    riding: str = ''
    url: str = ''
    url_desc: str = ''

    matches = re.match(candidate_exp, c)
    if matches is not None:
        headshot = matches[1]
        name = matches[2]
        riding = matches[3]
        url = matches[4]
        url_desc = matches[5]
    else:
        print (f'The html was not matched: {c}\n')

    return (headshot, name, riding, url, url_desc)

def clean_html(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
