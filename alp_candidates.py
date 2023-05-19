import re

htmlfile = 'alp_candidates.html'
csvfile = 'alp_candidates.csv'
pattern = r'^<a class=.+?\shref=\"(.+?)\">(.+?)\|(.+?)<\/a>'


def parse_candidates_html():
    headshot: str = ''
    name: str = ''
    riding: str = ''
    url: str = ''

    count = 0
    expected_count = 12
    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csv:
        for can in html.readlines():
            # skip the first line should not be tagged as data. should be a header.
            count = count + 1
            matches = re.match(pattern, can)
            if matches is not None:
                url = matches[1]
                name = matches[2]
                riding = matches[3]
            else:
                print(f'The pattern was not matched: {can}\n')
                assert False

            csv.write(f'ALP\t{name}\t{riding}\t{url}\t{headshot}\n')
            csv.flush()
        csv.close()
        print(f'ALP: There were {count} candidates found. Expected {expected_count}')


def clean_html(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
