import re
import json
from openpyxl import load_workbook


def parse_party_html(htmlfile='ab_parties.html', csvfile='ab_parties.csv'):
    with open(htmlfile, "rt") as h, open(csvfile, "wt") as csv, open('people.csv', 'wt') as ppl:
        for p in h.readlines():
            p = clean_html(p)
            # print (p)
            party = parse_fields(p)
            # print(party)
            csv.write(party[0])
            csv.write('\t')
            csv.write(party[1])
            csv.write('\t')
            csv.write(party[2])
            csv.write('\t')
            csv.write(party[3])
            csv.write('\t')
            csv.write(party[4])
            csv.write('\t')
            csv.write(party[5])
            csv.write('\t')
            csv.write(party[6])
            csv.write('\t')
            csv.write(party[7])
            csv.write('\t')
            csv.write(party[8])
            csv.write('\n')

            csv.flush()

            people = party[9]
            for p in people:
                ppl.write(p[0])
                ppl.write('\t')
                ppl.write(p[1])
                ppl.write('\t')
                ppl.write(p[2])
                ppl.write('\n')
                ppl.flush()

    h.close()
    csv.close()
    ppl.close()


def parse_fields(li: str):
    name_exp = '^<li><a href=.+?>(.+?)<\/a>'
    short_name_exp = '\s\((.+?)\)$'
    logo_exp = '^<li>.+?src="(.+?)<\/p>'
    data_exp = '^<li>.+?<\/div><div><p>(.+)<br>'  # unstructured data fields, officers, city, phone etc
    data_exp_alt = '^<li>.+?<\/a>.+?<div><p>(.+)<br>'  # try a simpler exp for cases missing some markup
    city_postal_exp = '.+<br>(.+?), (AB|Alberta) .*?([A-Z][0-9][A-Z] [0-9][A-Z][0-9])$'
    staff_exp = r'^(.+?),\s?(Leader|Chief Financial Officer|President|Interim Leader)$'
    email_exp = r'.+Email:.+<a href="(mailto:.+?)">(.+?)<\/a>.+?<\/li>$'  # prob one of the last fields
    web_exp = r'^<a href="(.+)">(.+)<\/a>$'

    name = ''
    short_name = ''
    logo = ''
    address = ''
    city = ''
    prov = ''
    pc = ''
    email_link = ''
    web_link = ''
    people = []
    phone = []

    matches = re.match(name_exp, li)
    if matches is not None:
        name = str(matches[1])
        # print (name)

    matches = re.findall(short_name_exp, name)
    if matches is not None:
        short_name = str(matches[0])

    matches = re.match(logo_exp, li)
    if matches is not None:
        logo = str(matches[1])
        # print (logo)

    matches = re.match(data_exp, li)
    if matches is not None:
        data = str(matches[1])
        data_fields = data.split('<br>')
    else:
        matches = re.match(data_exp_alt, li)
        if matches is not None:
            data = str(matches[1])
            data_fields = data.split('<br>')
        else:
            data = ''
            assert (False)

    if len(data_fields):
        for f in data_fields:
            matches = re.match(staff_exp, f)
            if matches is not None:
                person = str(matches[1])
                position = str(matches[2])
                people.append((short_name, person, position))
                continue

            matches = ['Street', 'PO', 'PO Box']
            if any([x in f for x in matches]):
                address = f
                continue

            matches = re.match(city_postal_exp, f)
            if matches is not None:
                city = str(matches[1])
                prov = str(matches[2])
                pc = str(matches[3])
                continue

            matches = ['Phone:', 'Toll Free:', 'Fax:']
            if any([x in f for x in matches]):
                t = f.split(':')
                phone.append((short_name, t[0], t[1]))
                continue

            matches = re.match(web_exp, f)
            if matches is not None:
                web_link = str(matches[1])

    matches = re.match(email_exp, li)
    if (matches is not None):
        email_link = str(matches[1])
        # email_desc = str(matches[2])

    # print(people)
    # print(f'City: {city} Prov: {prov}  Postal: {pc}')
    # print('')

    # print(f'{name}\t{logo}')
    # print(f'\t{data}')

    return name, short_name, logo, address, city, prov, pc, email_link, web_link, people, phone


def clean_html(p: str):
    """
    Clean yp the html string to make the regex matching easier
    :param p: html string
    :return: cleaned string
    """
    p = p.replace(' class="accordion-navigation"', '')
    p = p.replace(' role="button"', '')
    p = p.replace(' aria-expanded="false"', '')
    # aria-controls="acc1"
    # e.g. re.sub(r'(?is)</html>.+', '</html>', article)
    p = re.sub(r'(?is) aria-controls="acc[0-9]{1,2}"', '', p)
    p = re.sub(r'(?is) id="acc[0-9]{1,2}"', '', p)
    p = p.replace(' class="content"', '')
    p = p.replace(' class="row collapse--sm"', '')
    p = p.replace(' class="medium-4 large-4"', '')
    p = p.replace(' class="attachment-party-logo size-party-logo" alt="" decoding="async" loading="lazy"', '')
    p = p.replace(' class="medium-8 large-8"', '')
    p = re.sub(r'(?is) srcset="(.+?)</p>', '</p>', p)
    p = p.replace(' target="_blank" rel="noopener"', '')
    p = p.replace('<strong>', '')
    p = p.replace(r'<\/strong>', '')

    return p


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_party_html()
