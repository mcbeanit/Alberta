import re


def parse_candidates_html():
    with open('gpa_candidates.html', 'rt') as html, open('gpa_candidates.csv', 'wt') as csv:
        count = 0
        pattern = 'src=.(https.+png)'
        short_name = 'gpa'
        for c in html.readlines():
            count = count + 1
            matches = re.findall(pattern, c)
            if matches is not None:
                url = str(matches[0])
                csv.write(f'{short_name}\t')
                csv.write(f'{url}\t')
                csv.write(f'')  # where the name would go if it was in their html.
                csv.write('\n')
            else:
                print('not matched')

        html.close()
        csv.close()
        print(f'There were {count} candidates found. See gpa_candidates.csv ')


if __name__ == '__main__':
    parse_candidates_html()
