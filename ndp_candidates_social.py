import re
import csv

social_html = 'ndp_candidates_social.html'
csv_file = 'ndp_candidates_social.csv'
social_exp = r'^<li class=\"follow-link-item\">.+?href=\"(https://.+?)\"'
def parse_candidates_html():
    file = open(social_html, newline='')
    reader = csv.reader(file, delimiter='\t')
    data = [row for row in reader]
    assert data
    file.close()

    with open(csv_file, 'wt') as csv_out:
        for html in  data:
            name = html[0]
            riding = html[1]
            li = html[2]
            link = ''
            platform = ''

            matches = re.match(social_exp, li)
            if matches is not None:
                link = matches[1]
                if 'twitter' in link:
                    platform = "Twitter"
                if 'instagram' in link:
                    platform = 'Instagram'
                if 'facebook'  in link:
                    platform = 'Facebook'
            else:
                print(f'{name}: links were not found')
            csv_out.write(f'{name}\t{riding}\t{platform}\t{link}\n')












if __name__ == '__main__':
    parse_candidates_html()