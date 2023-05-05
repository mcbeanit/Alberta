import re

pattern = r'^<div\sclass=\"plank-container-inner\">.+?<a href=\"(.+?)\".+?<img.+?src=\"(.+?)\"\salt=\"(.+?)\sfor\s(.+?)\"><\/a>'


def parse_candidates_html():
    with open('gpa_candidates.html', 'rt') as html, open('gpa_candidates.csv', 'wt') as csv:
        count = 0
        expected_count = 32
        short_name = 'gpa'
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
                csv.write(f'{short_name}\t{name}\t{riding}\t{url}\t{headshot}\n')
            else:
                print('not matched')

        html.close()
        csv.close()
        print(f'GPA: There were {count} candidates found. Expected: {expected_count}')


if __name__ == '__main__':
    parse_candidates_html()
