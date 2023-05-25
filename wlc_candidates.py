import re
import csv

party_name = "WLC"
html_filename = 'wlc_candidates.html'
csv_filename = 'wlc_candidates.csv'
candidate_url_expr = r'^<article.+?<div class=\"et_pb_image_container\"><a href=\"(.+?)\"'
name_riding_expr = r'^<article.+?<h2 class=\"entry-title\"><a href=\".+?\">(.+?)<\/a><\/h2>.+?<p>(.+?)<\/p>'
headshot_expr = r'^<article.+?src=(\"https.+?.jpg)\?'
expected_count = 15  # registered candidates, but only 9 on website now (24-may-2023)
def parse_candidates_html():
    with open(html_filename, 'rt') as html, open(csv_filename, 'wt') as csv_file:
        count = 0
        for c in html.readlines():
            matches = re.match(candidate_url_expr, c)
            if matches:
                url = matches[1].strip();
            else:
                print(f'not matched: {c}')
            matches = re.match(name_riding_expr, c)
            if matches:
                name = matches[1]
                riding = matches[2]
            else:
                print(f'name riding not matched')
            matches = re.match(headshot_expr, c)
            if matches:
                headshot = matches[1]
            else:
                print('headshot not matched')

            count = count + 1
            csv_file.write(f'{party_name}\t{name}\t{riding}\t{url}\t{headshot}\n')

    html.close()
    csv_file.close()
    print(f'wlc_candidates.py: there were {count} candidates found.')




if __name__ == '__main__':
    parse_candidates_html()
