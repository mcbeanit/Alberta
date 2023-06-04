import re

html_filename = 'ab_2023_party_standings.html'
csv_filename = 'ab_2023_party_standings.csv'
csv_pop_vote = 'ab_2023_pop_vote_party.csv'
expr = r'^<td data-th=\"(.+?)\".+?\"ward-votes-(.+?)\".+?>([0-9,]+)<\/span><\/td>$'
expr_riding = '^([0-9]+)-([0-9]+)$'


def import_results_html():
    candidate_count = 0
    total_votes = 0
    expected_votes: int = 1763441

    with open(html_filename, 'rt') as h, open(csv_filename, 'wt') as c:
        for ht in h.readlines():
            matches = re.match(expr, ht)
            if matches:
                party = matches[1]
                riding_code = matches[2]
                matches_r = re.match(expr_riding, riding_code)
                riding_number = matches_r[1]
                votes = int(matches[3].replace(',', ''))
                candidate_count = candidate_count + 1
                total_votes = total_votes + votes
                c.write(f'{party}\t{riding_number}\t{votes}\n')
    h.close()
    c.close()

    print(f'There are {candidate_count} candidates with votes')
    print(f'Total votes: {total_votes} (Expected: {expected_votes})')


def popular_vote_by_party():
    with open(csv_filename, 'rt') as csvfile:
        for row in csvfile.readlines():
            flds = row.split('\t')
            party = flds[0].strip()
            votes = flds[2].strip()
            print(f'{party} got {votes} votes')


if __name__ == '__main__':
    import_results_html()
    popular_vote_by_party()
