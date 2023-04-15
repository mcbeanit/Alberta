import re
import json
from openpyxl import load_workbook

def parse_party_html(htmlfile='ab_parties.html', csvfile='ab_parties.csv'):

    with open(htmlfile, "rt") as h:
        for p in h.readlines():
            p = clean_html(p)
            # print (p)
            parse_fields(p)

def parse_fields(li:str):
    name_exp = '^<li><a href=.+?>(.+?)<\/a>'
    short_name_exp = '\((.+?)\)$'
    logo_exp = '^<li>.+?src="(.+?)<\/p>'
    data_exp = '^<li>.+?<\/div><div><p>(.+)<br>'  # unstructured data fields, officers, city, phone etc
    data_exp_alt = '^<li>.+?<\/a>.+?<div><p>(.+)<br>'  # try a simpler exp for cases missing some markup
    city_postal_exp = '.+<br>(.+?), (AB|Alberta) .*?([A-Z][0-9][A-Z] [0-9][A-Z][0-9])$'
    staff_ex[ = '^(.+?),\s?(Leader|Chief Financial Officer|President|Interim Leader)$'

    matches = re.match(name_exp, li)
    if matches is not None:
        name = str(matches[1])
        # print (name)
    else:
        name = ''
        

    matches = re.match(short_name_exp, name)
    if matches is not None:
        short_name = str(matches[1])
    else:
        short_name = ''


    matches = re.match(logo_exp, li)
    if matches is not None:
        logo = str(matches[1])
        # print (logo)
    else:
        logo = ''
        # print('The logo file was not found')

    matches = re.match(data_exp, li)
    if matches is not None:
        data = str(matches[1])
        data_fields = data.split('<br>')
        for f in data_fields:
            print(f'Field: {f}')
        # print(data)
    else:
        matches = re.match(data_exp_alt, li)
        if matches is not None:
            data = str(matches[1])
            data_fields = data.split('<br>')
            for f in data_fields:
                print(f'Field: {f}')
        else:
            data = ''
            assert (False)

    matches = re.match(city_postal_exp, data)
    if matches is not None:
        pass
        #city = str(matches[1])
        #prov = str(matches[2])
        #pc =  str(matches[3])
    else:
        pass
        # print(f"failed city match: {data}")
        city = ''
        pc = ''
        prov = ''


    # print(f'City: {city} Prov: {prov}  Postal: {pc}')
    # print('')

    # print(f'{name}\t{logo}')
    # print(f'\t{data}')
def clean_html(p:str):
    """
    Clean yp the html string to make the regex matching easier
    :param p: html string
    :return: cleaned string
    """
    p = p.replace(' class="accordion-navigation"', '')
    p = p.replace(' role="button"','')
    p = p.replace(' aria-expanded="false"','')
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

    return p

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_party_html()



