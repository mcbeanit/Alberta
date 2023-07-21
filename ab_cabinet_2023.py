import re
import csv

flds_expr = r'^<tr><td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/td><\/tr>$'
ministry_expr_wlink = r'^<a href=\"(.+?)\".+?>(.+?)<\/a>(.+?)?$'
member_expr = r'^<a href=\"(.+?)\".+?>(.+?)<\/a>(.+?)?$'

def parse_party_html(htmlfile='ab_cabinet_2023.html', csvfile='ab_cabinet_2023.csv'):
    with open(htmlfile, "rt") as h, open(csvfile, "wt") as csv:
        count = 0
        for tr in h.readlines():
            count = count + 1
            matches = re.match(flds_expr, tr)
            ministry: str = ''
            wiki: str = ''
            member: str = ''
            apppointed_date: str = ''

            if matches:
                td1 = matches[1]
                td2 = matches[2]
                td3 = matches[3]
                # csv.write(f'{td1},{td2},{td3}\n')

                matches = re.match(ministry_expr_wlink, td1)

                try:
                    if matches:
                        wiki = matches[1]
                        if matches[3]:
                            ministry = matches[2] + matches[3]
                        else:
                            ministry = matches[2]
                    else:
                        ministry = td1
                        wiki = ''
                except TypeError:
                    print(f'Error Checking: {td1}')

                matches = re.match(member_expr, td2)
                if matches:
                    member = matches[2]

                if td3:
                    apppointed_date = td3
                else:
                    apppointed_date = 'June 9, 2023'

                csv.write(f'{ministry}\t{wiki}\t{member}\t{apppointed_date}\n')

if __name__ == '__main__':
    parse_party_html()
