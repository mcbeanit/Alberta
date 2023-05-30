import operator
import re
import csv


htmlfile = 'alp_candidates.html'
csvfile = 'alp_candidates.csv'
pattern = r'^<a class=.+?\shref=\"(.+?)\">(.+?)\|(.+?)<\/a>'


def parse_candidates_html():
    headshot: str = ''
    name: str = ''
    riding: str = ''
    url: str = ''

    count = 0
    expected_count = 13
    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csvout:
        # if header -> csvout.write('party\tname\triding\turl\n')
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

            csvout.write(f'ALP\t{name}\t{riding}\t{url}\t{headshot}\n')
            csvout.flush()
        csvout.close()
        print(f'alp_candidates.py: There were {count} candidates found. Expected {expected_count}')

        # sort the csv file
        with open(csvfile, 'rt') as r:
            reader = csv.reader(r, delimiter='\t')
            list = sorted(reader, key=operator.itemgetter(2),reverse=False)

        # rewrite the sorted file
        with open(csvfile, 'wt') as s:
            for p in list:
                s.write(f'{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\n');



def clean_html(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
