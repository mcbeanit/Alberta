import re
import csv
import operator

def parse_candidates_html():
    """
    Read the html <section> tags from the ucp candidate list html content and
    parse the fields of interest and save to a csv file.
    :return: None
    """
    expected_count = 86
    htmlfile = "ucp_candidates.html"
    csvfile = "ucp_candidates.csv"
    short_name = 'UCP'

    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csvout:
        count = 0
        for c in html.readlines():
            count = count + 1
            c = parse_candidate(c)
            csvout.write(f'{short_name}\t')
            csvout.write(f'{c[1]}\t')
            csvout.write(f'{c[2]}\t')
            csvout.write(f'{c[3]}\t')
            csvout.write(f'{c[0]}\n')
        print(f"ucp_candidates.py: There were {count} candidates found and {expected_count} expected.")
    html.close()
    csvout.close()

    with open(csvfile, 'rt') as r:
        reader = csv.reader(r, delimiter='\t')
        list = sorted(reader, key=operator.itemgetter(2), reverse=False)

    # rewrite the sorted file

    with open(csvfile, 'wt') as s:
        for p in list:
            s.write(f'{p[0]},{p[1]},{p[2]}\t{p[3]}\n');


def parse_candidate(c: str):
    pattern = r'^<section><img src=\"(.+?)\"><\/div><div>(.+?)<\/div><div>(.+?)<\/div><div><a href=\"(.+?)\"><\/a><\/div><\/section>$'
    headshot: str = ''
    name: str = ''
    riding: str = ''
    url: str = ''

    matches = re.match(pattern, c)
    if matches is not None:
        headshot = matches[1]
        name = matches[2]
        riding = matches[3]
        url = matches[4]

    return headshot,name,riding,url


def clean_html(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
