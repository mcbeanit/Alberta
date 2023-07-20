import re
import csv

def parse_party_html(htmlfile='ab_cabinet_2023.html', csvfile='ab_cabinet_2023.csv'):
    with open(htmlfile, "rt") as h, open(csvfile, "wt") as csv:
        count = 0
        for p in h.readlines():
            count = count + 1
            





if __name__ == '__main__':
    parse_party_html()


