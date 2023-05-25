import re

ab_338_html_filename = 'ab_338_ridings.html'
ab_338_csv_filename = 'ab_338_ridings.csv'
tr_expr = r'^<tr>.*?<td.+?><a href=\"(https:.+?)\".+?>(.+?)<\/a><\/td><td.+?>(.+?)<\/td><td.+?>(.+?)<\/td>.*?<\/tr>$'


def parse_riding_polls_html():
    with open(ab_338_html_filename, 'rt') as html, open(ab_338_csv_filename, 'wt') as csvfile:
        count = 0
        for tr in html.readlines():
            matches = re.match(tr_expr, tr)
            if matches:
                csvfile.write(f'{matches[2]},{matches[1]},{matches[4]}\n')
                count = count + 1
            else:
                print(f'not matched: {tr}\n')
    # html.close()
    # csvfile.close()
    print(f'ab_338_ridings.py: There were {count} ridings found with polls.')


if __name__ == '__main__':
    parse_riding_polls_html()
