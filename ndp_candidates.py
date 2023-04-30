import re


candidate_exp = r'^<div><div><article><div><img data-src=\"(.+?)\"></div><h1>(.+?)</h1><h2>(.+?)</h2><a href=\"(.+?)\"><span>(.+?)</span></a>'
def parse_candidates_html(htmlfile='ndp_candidates.html', csvfile='ndp_candidates.csv'):
    """
    Read the html from the NDP Candidate list and extract relevant
    fields into a csv file.
    :param htmlfile:
    :param csvfile:
    :return:
    """
    count = 0
    with open(htmlfile, "rt") as html, open(csvfile, 'wt') as csv:
        for c in html.readlines():
            count = count + 1
            c = clean_html(c)
            candidate = parse_candidate(c)
            print(f'{candidate[1]}')
            csv.write('NDP\t')
            csv.write(f'{candidate[1]}\t')
            csv.write(f'{candidate[2]}\t')
            csv.write(f'{candidate[3]}\t')
            csv.write(f'{candidate[0]}\t')
            csv.write('\n')

    html.close()
    csv.close()

    print(f'There are {count} candidates. \n')


def parse_candidate(c: str):
    headshot: str = ''
    name: str = ''
    riding: str = ''
    url: str = ''
    url_desc: str = ''

    matches = re.match(candidate_exp, c)
    if matches is not None:
        headshot = matches[1]
        name = matches[2]
        riding = matches[3]
        url = matches[4]
        url_desc = matches[5]
    else:
        print (f'The html was not matched: {c}\n')

    return (headshot, name, riding, url, url_desc)

def clean_html(c: str):
    return c


if __name__ == '__main__':
    parse_candidates_html()
