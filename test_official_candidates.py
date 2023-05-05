import pytest
import re

exp_tbody = r'^^<table.+?<tbody>(.+)<\/tbody>'
test_row = '<table class="has-alt-colors"><thead><tr><th>Candidate</th><th>Official Agent</th></tr></thead><tbody><tr><td style="width:33.33%; min-width:150px;">DRUH FARRELL<br>ALBERTA NDP<br><a href="https://www.albertandp.ca/" target="_blank">www.albertandp.ca</a></td><td style="min-width:300px;">Harris Kirshenbaum<br>Phone: <a href="tel:7804742415">780-474-2415</a><br>Address: 201 - 10544 114 STREET NW, EDMONTON T5H3J7</td></tr><tr><td style="width:33.33%; min-width:150px;">DEMETRIOS NICOLAIDES<br>UNITED CONSERVATIVE PARTY<br><a href="https://www.unitedconservative.ca/" target="_blank">www.unitedconservative.ca</a></td><td style="min-width:300px;">Blackett Blackett<br>Phone: <a href="tel:5878850543">587-885-0543</a><br>Address: 125, 6311 BOWNESS RD NW, CALGARY T3B0E4</td></tr></tbody></table>'
exp_fields = r'^<tr><td\s.+?>(.+?)<br>(.+?)<br>.+?<td\s.+?>(.+?)<br>.+<\/td><\/tr>$'

def test_match_rows():
    # extact the list of <tr>
    matched = re.match(exp_tbody, test_row)
    assert matched
    body = matched[1]
    assert body
    body = re.sub('</tr>', '</tr>\n', body)
    body = body.strip().split('\n')
    count = 0
    for b in body:
        count = count + 1
        matched = re.match(exp_fields, b)
        if matched is not None:
            print()
            print(f'{matched[1]}'.title())
            print(f'{matched[2]}'.title())
            print(f'{matched[3]}'.title())
