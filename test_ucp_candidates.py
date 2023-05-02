import pytest
import re
import csv
import gender_guesser

csv_file = 'ucp_candidates.csv'
def test_read_candidate_urls():
    urls = []
    file = open(csv_file, newline='')
    reader = csv.reader(file, delimiter='\t')
    data = [row for row in reader]
    assert data
    count = 0
    for row in data:
        count = count + 1
        url = str(row[3])
        urls.append(url)
        # print(url)

    file.close()
    assert len(urls) == 87
    assert count == 87
    print(urls)

def test_gender_guesser():
    g =  gender_guesser.guess('sfdsfdsfdsfds mom fdsfdsfdsf')
    assert g == 'F'
