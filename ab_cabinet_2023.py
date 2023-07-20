import re
import csv

flds_expr = r'^<tr><td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/td><\/tr>$'


def parse_party_html(htmlfile='ab_cabinet_2023.html', csvfile='ab_cabinet_2023.csv'):
    with open(htmlfile, "rt") as h, open(csvfile, "wt") as csv:
        count = 0
        for tr in h.readlines():
            count = count + 1
            matches = re.match(flds_expr, tr)
            if matches:
                print(f'{matches[1]},{matches[2]},{matches[3]}\n')



if __name__ == '__main__':
    parse_party_html()
