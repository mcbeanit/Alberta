import re
import csv

htmlfilename = 'ab_ridings.html'
csvfilename = 'ab_ridings.csv'
pattern = '^<tr><td>([0-9]+?)<\/td><td>(.+?)<\/td><td>([0-9\*]{4,5})<\/td><td>(.+?)<\/td><td bgcolor=\"(' \
          '.+?)\"><\/td><td>(.+?)<\/td><td>([0-9,]+?)<\/td>.*<\/tr>$'
patternTitle = '^<a href="(.+?)"\s.*?title=".+?">(.+?)<\/a>$'
patternMLA = '^<span data-sort-value=\"(.+?)\".*$'

def import_html():
    count = 0
    with open(htmlfilename, 'rt') as f:
        with open(csvfilename, "wt") as w:
            for row in f:
                if row.startswith('<tr>'):
                    count = count + 1
                    matches = re.match(pattern, row)
                    if matches is not None:
                        w.write(str(matches[1]))
                        w.write('\t')
                        matchesTitle = re.match(patternTitle, str(matches[2]))
                        if matchesTitle is not None:
                            w.write(str(matchesTitle[1]))
                            w.write('\t')
                            w.write(str(matchesTitle[2]))
                            w.write('\t')
                        w.write(str(matches[3]))
                        w.write('\t')
                        mla = str(matches[4])
                        matchesMLA = re.match(patternMLA, mla)

                        # mla name  (last, first)
                        w.write(str(matchesMLA[1]))
                        w.write('\t')

                        # party color is html hex
                        w.write(str(matches[5]))
                        w.write('\t')

                        # party name
                        w.write(str(matches[6]))
                        w.write('\t')

                        # population
                        w.write(str(matches[7]))

                        w.write('\n')

                    else:
                        w.write(f'Not matched: {row}')
        w.close()
    f.close()

if __name__ == '__main__':
    import_html()
