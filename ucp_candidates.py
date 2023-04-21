import re
import os

csv_file =  'ucp_candidates.csv'
html_file = 'ucp_candidates.html'
not_running_file = 'ucp_not_running.csv'

pattern = r'^<article><figure><a href=\"(.+?)\"><img src=\"(.+?)\"></a></figure><figcaption><h2>.+?>(.+?)</a></h2><p>(.+?)</p>'
count = 0
short_name = 'UCP'
not_running = ['Leela Aheer', 'Richard Gotfried', 'Ron Orr', 'Pat Rehn', 'Roger Reid', 'Brad Rutherford', 'Mark Smith', 'Sonya Savage', 'Rajan Sawhney', 'Travis Toews', 'Tracy Allard']
lost_nom = ['Tany Yao', 'David Hanson', 'Dave Hanson']

def parse_candidates_html():
    if os.path.exists(not_running_file):
        os.remove(not_running_file)

    with open(html_file, 'rt') as html, open(csv_file, 'wt') as csv:
        global count
        for c in html.readlines():
            count = count + 1
            c = clean(c)
            candidate = parse_candidate(c)
            if (candidate[1] not in not_running) and (candidate[1] not in lost_nom):
                # print(f'Creating csv for {candidate[1]}')
                csv.write(f'{short_name}\t')
                csv.write(f'{candidate[1]}\t')
                csv.write(f'{candidate[2]}\t')
                csv.write('Yes\t\t')
                csv.write(f'{candidate[3]}\t')
                csv.write(f'{candidate[4]}\n')
            else:
                print(f"Not running: {candidate[1]}\n")
                with open(not_running_file,'a') as nr:
                    nr.write(f'{short_name}\t')
                    nr.write(f'{candidate[1]}\t')
                    nr.write(f'{candidate[2]}\t')
                    nr.write('Yes\t\t')
                    nr.write(f'{candidate[3]}\t')
                    nr.write(f'{candidate[4]}\n')
                    nr.close()

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
