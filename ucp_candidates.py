import re
import json


def parse_candidates_html():
    """
    Read the html <section> tags from the ucp candidate list html content and
    parse the fields of interest and save to a csv file.
    :return: None
    """
    expected_count = 87
    htmlfile = "ucp_candidates.html"
    csvfile = "ucp_candidates.csv"

    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csv:
        count = 0
        for c in html.readlines():
            count = count + 1
            c = parse_candidate(c)
            csv.write(f'{c[1]}\t')
            csv.write(f'{c[2]}\t')
            csv.write(f'{c[3]}\t')
            csv.write(f'{c[0]}\n')
            csv.flush()
        print(f"UCP: There were {count} candidates found and {expected_count} expected.")
    html.close()
    csv.close()


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
