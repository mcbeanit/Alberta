import re
import csv
import os

bio_html_file = 'gpa_candidates_spider_more.html'
social_html_file = 'gpa_candidates_social.html'
social_csv_file = 'gpa_candidates_social.csv'
bio_exp = r'^<p><span\s.+?>(.+?)<\/span><\/p'
bio_csv_file = 'gpa_candidates_more.csv'
link_exp = r'^<a href=\"(http[s]?.+?)\"'

def parse_candidates_bio_html():
    """
    Read the html for the bio's and extract the text
    Read the html for the social media links and extract them
    :return: none
    """

    file = open(bio_html_file, newline='')
    reader = csv.reader(file, delimiter='\t')
    data = [row for row in reader]
    assert data
    names = []
    bio_text = ''
    with open(bio_csv_file, 'wt') as bio_csv:
        for row in data:
            short_name = row[0]
            name = row[1]
            riding = row[2]
            html = row[3]
            html = html.replace('<p>', '')
            html = re.sub('style=".+?"', '', html)
            html = re.sub(r'<span\s+?>', '', html)
            html = html.replace('</p>', '')
            html = html.replace('</span>', '')
            html = html.replace('<span>', '')
            html = html.replace(u'\xc2', '')
            html = html.replace(u'\xa0', '')
            html = html.replace('<br>', '')
            html = html.strip()
            bio_csv.write(f'{short_name}\t{name}\t{riding}\t{html}\n')
        bio_csv.close()

def parse_candidates_social_html():
    file = open(social_html_file , newline='')
    reader = csv.reader(file, delimiter='\t')
    data = [row for row in reader]
    assert data

    social = ''
    with open(social_csv_file, 'wt') as social_csv:
        for row in data:
            short_name = row[0]
            name = row[1]
            riding = row[2]
            social = row[3]
            matches = re.match(link_exp, social)
            platform = ''
            if matches is not None:
                link = matches[1]
                if '.' 'png' not in matches[1]:
                    if 'twitter' in link:
                        platform = 'Twitter'
                    if 'facebook' in link:
                        platform = 'Facebook'
                    if 'instagram' in link:
                        platform = 'Instagram'
                    social_csv.write(f'{short_name}\t{name}\t{riding}\t{platform}\t{link}\n')
        social_csv.close()






if __name__ == '__main__':
    parse_candidates_bio_html()
    parse_candidates_social_html()