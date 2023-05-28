import re
import csv
import operator

pattern = r'^<div\sclass=\"plank-container-inner\">.+?<a href=\"(.+?)\".+?<img.+?src=\"(.+?)\"\salt=\"(.+?)\sfor\s(.+?)\"><\/a>'
csvfile = 'gpa_candidates.csv'

def parse_candidates_html():
    with open('gpa_candidates.html', 'rt') as html, open(csvfile, 'wt') as csvout:
        count = 0
        expected_count = 41
        short_name = 'GPA'
        for c in html.readlines():
            count = count + 1
            matches = re.match(pattern, c)
            name = ''
            riding = ''
            url = ''
            headshot = ''
            if matches is not None:
                url = str(matches[1])
                name = str(matches[3])
                riding = str(matches[4])
                headshot = str(matches[2])
                csvout.write(f'{short_name}\t{name}\t{riding}\t{url}\t{headshot}\n')
            else:
                print('not matched')

        html.close()
        csvout.close()
        print(f'gpa_candidates.py: There were {count} candidates found. Expected: {expected_count}')

        with open(csvfile, 'rt') as r:
            reader = csv.reader(r, delimiter='\t')
            list = sorted(reader, key=operator.itemgetter(2), reverse=False)

            # rewrite the sorted file
        with open(csvfile, 'wt') as s:
            for p in list:
                s.write(f'{p[0]},{p[1]},{p[2]}\t{p[3]}\t{p[4]}\n');


if __name__ == '__main__':
    parse_candidates_html()
