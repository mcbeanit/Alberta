import re
import json

csv_file =  'ucp_candidates.csv'
html_file = 'ucp_candidates.html'
pattern = r'^<article><figure><a href=\"(.+?)\"><img src=\"(.+?)\"></a></figure><figcaption><h2>.+?>(.+?)</a></h2><p>(.+?)</p>'
count = 0
short_name = 'UCP'
not_running = ['Leela Aheer', 'Richard Gotfried', 'Ron Orr', 'Pat Rehn', 'Roger Reid', 'Brad Rutherford', 'Mark Smith', 'Sonya Savage', 'Rajan Sawhney', 'Travis Toews', 'Tracy Allard']
lost_nom = ['Tany Tao', 'Dave Hanson']
def parse_candidates_html():

    with open(html_file, 'rt') as html, open(csv_file, 'wt') as csv:
        global count
        for c in html.readlines():
            count = count + 1
            c = clean(c)
            candidate = parse_candidate(c)
            if not candidate[1] in not_running:
                print(f'Creating csv for {candidate[1]}')
                csv.write(f'{short_name}\t')
                csv.write(f'{candidate[1]}\t')
                csv.write(f'{candidate[2]}\t')
                csv.write('Yes\t\t')
                csv.write(f'{candidate[3]}\t')
                csv.write(f'{candidate[4]}\n')
            else:
                print(f"Not running: {candidate[1]}\n")

            csv.flush()


def parse_candidate(c: str):
    matches = re.match(pattern, c)
    if matches is not None:

        headshot: str = ''
        name: str = ''
        riding: str = ''
        url: str = ''

        url = str(matches[1])
        headshot = str(matches[2])
        name = str(matches[3])
        riding = str(matches[4])

        return short_name, name, riding, url, headshot

    else:
        print ('The pattern was not matched: \n')
        print (f'{c}\n')


    return c


def clean(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
