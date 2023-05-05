import re
import datetime

"""
Read the official_candidates.html file and do some more processing to get 
a cvs file (official_candidates.csv/
"""
name = 'Official Candidates'
exp_tbody = r'^^<table.+?<tbody>(.+)<\/tbody>'
exp_fields = r'^<tr><td\s.+?>(.+?)<br>(.+?)<br>.+?<td\s.+?>(.+?)<br>.+<\/td><\/tr>$'


def parse_candidates_html(htmlfile='official_candidates.html', csvfile='official_candidates.csv'):
    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csv:
        count = 0
        duplicates = []
        for c in html.readlines():
            matches = re.match(exp_tbody, c)
            if matches is not None:
                body = matches[1]
                body = re.sub('</tr>', '</tr>\n', body)
                body = body.strip().split('\n')

                for b in body:

                    matched = re.match(exp_fields, b)
                    if matched is not None:
                        name = matched[1].title()
                        if name not in duplicates:
                            count = count + 1
                            csv.write(f'{name}\t{matched[2].title()}\t{matched[3].title()}\n')
                            duplicates.append(name)
            else:
                csv.write(f'not matched({c})\n')
                assert False

        html.close()
        csv.close()
        print(f'There were {count} officially registered candidated\n')

if __name__ == '__main__':
    parse_candidates_html()
