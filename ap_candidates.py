import re
import csv
import operator

"""
After the spider gets the html for the Alberta Party candidates list, do some additional
parsing to get a csv list.
"""

# 1 = candidates url,  2 = candidates head shot url,  3 = candidate and riding
# format for name e.g. 'Barry Morishita for Brooks-Medicine Hat'
# the headshot link could be empty. check for None.
pattern1 = r'^<div><div><div><a href=\"(.*?)\"><img src=\"(.+?)\">.+?<h3>(.+?)<\/h3>'
# the html has no href for the candidates url
pattern2 = r'^<div><div><div><img src=\"(.+?)\">.+?<h3>(.+?)<\/h3>'
# 1 = candidates headshot, 2 = candidate and riding (as above)
html_file = 'ap_candidates.html'
csv_file = 'ap_candidates.csv'

def parse_candidates_html():
    with open(html_file,'rt') as html, open(csv_file, 'wt') as out:
        count = 0
        expected_count = 19

        for div in html.readlines():
            div = clean_html(div)

            candidate_url: str = ''
            candidate_headshot: str = ''
            name: str = ''
            riding: str = ''
            gender: str = ''

            matches = re.match(pattern1, div)
            if matches is not None:
                candidate_url:str = matches[1]
                candidate_headshot: str = matches[2]
                var = matches[3].split(' for ')
                if len(var)==2:
                    name: str = var[0]
                    riding: str = var[1]
                else:
                    # in this edge case the riding is not stated in the H3 heading. We'll
                    # pick it up later in the "more" processing
                    name: str = var[0]
                    riding = ''
                out.write(f'AP\t{name}\t{riding}\t{candidate_url}\t{candidate_headshot}\r{gender}')
            else:
                matches = re.match(pattern2, div)
                if matches is not None:
                    candidate_url: ''
                    candidate_headshot: str = matches[1]
                    var = matches[2].split(' for ')
                    name: str = var[0]
                    riding: str = var[1]
                    out.write(f'AP\t{name}\t{riding}\t{candidate_url}\t{candidate_headshot}\r{gender}')
                else:
                    print('ap_candidates.py: The pattern is not matched,')
                    assert False
            count = count + 1
        html.close()
        out.close()

    with open(csv_file, 'rt') as r:
        reader = csv.reader(r, delimiter='\t')
        list = sorted(reader, key=operator.itemgetter(2), reverse=False)

        # rewrite the sorted file
    with open(csv_file, 'wt') as s:
        for p in list:
            s.write(f'{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\n');

    print(f'ap_candidates.py: There were {count} candidates and {expected_count} expected.')

def clean_html(div:str):
    div = re.sub('class=".+?"', "", div)
    # div = div.replace('data-aos=""', '')
    # div = div.replace('data-aos-delay="', '')
    div = re.sub('>\\s+?<', '', div)
    div = div.replace(' For ', ' for ') # for some matching that's case sensitive.
    div = re.sub('\\s+?>', '>', div)

    return div






if __name__ == '__main__':
    parse_candidates_html()
