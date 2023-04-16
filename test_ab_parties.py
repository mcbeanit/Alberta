import pytest
import re
import json
from openpyxl import load_workbook


pattern = '^<li class="accordion-navigation".+?>(.+?)<\\/a><div class="content".+?<div.+?<\\/p><\\/div><div.+?<p>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br>(.+?)<br><a href="(.+?)">(.+?)<\\/a>.+<\\/div><\\/div><\\/li>$'

test1 = '<li class="accordion-navigation"><a href="#acc1" role="button" aria-controls="acc1" aria-expanded="false">Advantage Party of Alberta (APA)</a><div class="content" id="acc1"><div class="row collapse--sm"><div class="medium-4 large-4"><p><img width="250" height="90" src="https://www.elections.ab.ca/uploads/AlbertaAdvantageLogo-250x90.png" class="attachment-party-logo size-party-logo" alt="" decoding="async" loading="lazy" srcset="https://www.elections.ab.ca/uploads/./AlbertaAdvantageLogo-250x90.png 250w, https://www.elections.ab.ca/uploads/./AlbertaAdvantageLogo-400x144.png 400w, https://www.elections.ab.ca/uploads/./AlbertaAdvantageLogo-768x276.png 768w, https://www.elections.ab.ca/uploads/AlbertaAdvantageLogo.png 979w" sizes="(max-width: 250px) 100vw, 250px" /></p></div><div class="medium-8 large-8"><p>Marilyn Burns, Leader<br>Carol Nordlund Kinsey, President<br>Ron Malowany, Chief Financial Officer<br>559, 9768 170 Street<br>Edmonton, Alberta T5T 5L4<br><a href="https://albertaadvantageparty.ca" target="_blank" rel="noopener">https://albertaadvantageparty.ca</a></p><p><em>The Alberta Advantage Party made an application to the Chief Electoral Officer to change the party name to “Advantage Party of Alberta”. The request was received and approved, and the change was made effective February 9, 2022.</em></p></div></div></div></li>'
test2 = '<li class="accordion-navigation"><a href="#acc5" role="button" aria-controls="acc5" aria-expanded="false">Communist Party - Alberta (CP - A)</a><div class="content" id="acc5"><div class="row collapse--sm"><div><p>Naomi Rankin, Leader<br>Blyth Nuttall, Chief Financial Officer<br><a href="http://www.communistparty-alberta.ca/" target="blank">www.communistparty-alberta.ca</a><br>Phone: (780) 934-7893<br>Email: <a href="mailto:naomirankin@shaw.ca">naomirankin@shaw.ca</a></p></div></div></div></li>'


# ^<li class="accordion-navigation".+"false">(.+?)<\/a>.+?<div><p>(.+?)<br>(.+?)<br><a href="(.+?)".+?>(.+?)<\/a><br>(.+?)<br>(.+?)<a.+?<\/div><\/div><\/div><\/li>$



def test_should_match():
    """
    This test just checks if the typical html can be matched against the typical expression, and that
    the expected captured fields are as expected.
    """
    matches = re.match(pattern, test1)
    if matches is not None:
        f1 = str(matches[1])
        assert(f1 == 'Advantage Party of Alberta (APA)')
        f2 = str(matches[2])
        assert(f2 == 'Marilyn Burns, Leader')
        f3 = str(matches[3])
        assert(f3 == 'Carol Nordlund Kinsey, President')
        f4 = str(matches[4])
        assert(f4 == 'Ron Malowany, Chief Financial Officer')
        f5 = str(matches[5])
        assert(f5 == '559, 9768 170 Street')
        f6 = str(matches[6])
        assert(f6 == 'Edmonton, Alberta T5T 5L4')

    else:
        pytest.fail('Pattern 1 not matched')

def test_read_json():
    """
    How to read the standard json settings file and get a typical setting.
    """
    f = open('settings.json')
    settings = json.load(f)
    f.close()
    s = settings['settings']
    p1 = s[0]
    pattern = p1['pattern1']
    assert(len(pattern) > 0)
    assert(pattern.startswith('^'))


def test_read_excel():
    """
    Use the openpyxl library to check we can read the Alberta spreadsheet.
    """
    wb = load_workbook('C:\\Users\\owner\\OneDrive\\Alberta.xlsx')
    sheet = wb.worksheets[0]
    x = str(sheet['A2'].value)
    print(x)

def test_short_name():
    exp = '\\s\\((.+?)\\)$'
    case = 'Alberta New Democratic Party (NDP)'

    m = re.findall(exp,case)
    assert(m is not None)
    print(m)
    assert(str(m[0])=='NDP')

def test_email():
    exp = '^Email:.+<a href="mailto:(.+?)">(.+?)<\/a>$'
    case = 'Email:�<a href="mailto:info@albertaNDP.ca">info@albertaNDP.ca</a>'

    m = re.match(exp, case)
    assert(m is not None)