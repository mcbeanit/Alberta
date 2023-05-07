import re
import csv
import gender_guesser

"""
Extract the bio text from the raw html captured in alp_candidates_more.html
"""
html_file = 'alp_candidates_more.html'
csv_file = 'alp_candidates.more.csv'


def parse_candidates_html():
    with open(csv_file, 'wt') as csv_out:
        file = open(html_file, newline='')
        reader = csv.reader(file, delimiter='\t')
        data = [row for row in reader]
        assert data
        count = 0

        for h in data:
            name = str(h[0])
            riding = str(h[1])
            gender = ''
            b = str(h[2])
            b = clean_html(b)
            gender = gender_guesser.guess((b))
            csv_out.write(f'{name}\t{riding}\t{gender}\t{b}\n')

        file.close()
        csv_out.close()


def clean_html(c: str):
    c = c.replace(u'\xa0', '')
    c = c.replace('<div dir="ltr">', '')
    c = c.replace('<span>', '')
    c = c.replace('</span>', '')
    c = re.sub('class=".+?"', '', c)
    c = re.sub('style=".+?"', '', c)
    c = re.sub(r'<div\s+?>', '<div>', c)
    c = re.sub(r'<p\s+?>', '<div>', c)
    c = c.replace('<div>', '')
    c = c.replace('</div>', '')
    c = c.replace('<p>', '')
    c = c.replace('</p>', '')


    return c

# <div class="col-lg-6"><p style="font-weight: 400;">I’m Dylin Hauser. I have committed myself to raising my four children– 4 and 8 year old boys, a 10-year old girl and my oldest, a 12 year son who has been a huge influence on my campaign in the last election and on my life.</p><p style="font-weight: 400;">Much of my working life has been in the oilfields, almost all on a single rig, where for almost 7 years the crew stayed together, worked as a team, almost a family, and had not a single serious accident.But, as my family grew, my values changed. I’d followed in my father’s path without much thought, and upon his passing, the personal sacrifice away from my family lost its purpose. My son's mental health needs required more support. I left the rigs for a family life I struggled with missing. Kids grow up fast, and to me, soccer practice wasn't something I wanted to miss any more. Despite the significant financial cost of this change, for me the decision has been worthwhile<strong>.</strong>But I will forever respect those who stay in that life – we all make sacrifices in our different ways.</p><p style="font-weight: 400;">I understand the need for economic development, but we must allow and help our natural ecosystems to heal from human impacts and mitigate any future developments and minimize our environmental footprint.</p><p style="font-weight: 400;">I am running in this election because I am passionate about bringing options to voters, having my voice and those of others be heard before you choose your representative. I cannot promise every move I make will please you. I will think through every decision and I will be more than happy to be held accountable, to explain my rationale. I will be here to answer to my critics and share any good news I can bring.</p></div>


if __name__ == '__main__':
    parse_candidates_html()
