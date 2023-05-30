import re
import os
import csv

csv_file = 'ap_candidates_more.csv'
html_file = 'ap_candidates_more.html'
social_file = 'ap_candidates_social.html'

def parse_candidates_html():
    file = open(html_file, newline='')
    reader = csv.reader(file, delimiter='\t')
    data = [row for row in reader]
    assert data
    file.close()
    count = 0
    with open(csv_file, 'wt') as csv_out:
        for row in data:
            short_name = row[0]
            name = row[1]
            riding = row[2]
            bio_html = str(row[3])
            bio = clean_html(bio_html)
            csv_out.write(f'{short_name}\t{name}\t{riding}\t{bio}\n')
            csv_out.flush()
            count = count + 1
        csv_out.close()
    print(f'ap_candidates_more.py: there were {count} candidates found')


# e.g.
# <div class="row"><div class="col-md-8 offset-md-2"><h3></h3><p>Meet Kevin:</p><p> <span style="font-weight: 400;">Kevin Todd was born and raised in the community of Nanton and has had the privilege of raising his own family in the same town.</span></p><p><img style="float: right; max-width: 350px; padding-left: 20px; margin-top: -20px;" src="https://assets.nationbuilder.com/abparty/pages/3231/attachments/original/1683102411/Kevin_Todd_New_Website.jpg?1683102411" alt="None" width="500" height="571"></p><p><span style="font-weight: 400;">As his family has grown in this rural community, so has his commitment and service to the town and surrounding areas. Kevin has always been an active member of the community, whether it be volunteering with the Nanton Futures Foundation, Nanton Promoters, or the Nanton Golf Club. He also holds previous municipal political experience, having served on the Town Council for multiple years. Sharing his deep sense of neighbourhood involvement, Kevin's wife and both of his daughters are also an active part of the Nanton community.</span></p><p><span style="font-weight: 400;">Starting at the age of 12, Kevin travelled throughout Southern Alberta as both a hockey player and referee. He continues to travel through the riding as an avid outdoorsman and spends many weekends with his family camping, hunting, fishing, and quadding in the big, beautiful backyard that is the Rocky Mountains.</span></p><p><span style="font-weight: 400;">Kevin’s background in finance and his keen entrepreneurial spirit are what keeps him visiting all parts of the province and beyond as part of his work life. He never misses an opportunity to learn something new from a stranger, hop in his truck and drive a couple of hours for a cup of coffee, or have a chat about the importance of getting outdoors and getting back to nature.</span></p><p><span style="font-weight: 400;">As much as he enjoys collaborating with people from all walks of life and exploring the small-town gems Alberta has to offer, Kevin always finds himself drawn back to Nanton. To him, southern Alberta is the heart of the province, and it holds a special place for both himself and his family.</span></p><p> </p><p><strong>Visit us on Social Media</strong></p><table style="width: 16.2905%; border-collapse: collapse;" border="0"><tbody><tr style="height: 151px;"><td style="width: 84.2917%; height: 151px;"><img src="https://assets.nationbuilder.com/abparty/pages/3231/attachments/original/1683101734/FB_02.png?1683101734" alt="" width="130" height="130">  </td><td style="width: 473.835%; height: 151px;"><img src="https://assets.nationbuilder.com/abparty/pages/3231/attachments/original/1683101734/Twitter__01.png?1683101734" alt="" width="130" height="130">          </td></tr></tbody></table><p></p></div><!--Content Row End--><!--CA Event--><!--CA Blog--><!--Contact Section--><div class="col-md-8 offset-md-2"><h3></h3><p>Contact Us</p><p>If you'd like to help us get Kevin elected MLA for the Livingstone-Macleod constituency, please contact us: <br><a href="/cdn-cgi/l/email-protection#d2a6bdb6b6e0e2e0e192b3beb0b7a0a6b3a2b3a0a6abfcb1b3"><span class="__cf_email__" data-cfemail="d8acb7bcbceae8eaeb98b9b4babdaaacb9a8b9aaaca1f6bbb9">[email protected]</span></a></p><p></p></div><!--Contact Section End--><!--End Page Call to Action--><div class="col-md-8 offset-md-2 cta-section"><div class="cta-background"></div><div class="row"><div class="col-xl-4"><a href="/donate_to_kevin%0A"><div class="engage-card"><i class="far fa-id-card"></i><h4>Donate to Kevin </h4></div></a></div><div class="col-xl-4"><a href="/kevin_todd_lawn_signs"><div class="engage-card"><i class="far fa-id-card"></i><h4>Request a Lawn Sign</h4></div></a></div><div class="col-xl-4"><a href="volunteer_for_kevin"><div class="engage-card"><i class="far fa-id-card"></i><h4>Volunteer for Kevin</h4></div></a></div></div></div></div>
def clean_html(c: str):
    c = c.replace(u'\xa0', '')
    c = re.sub('class=".+?"', '', c)
    return c


if __name__ == '__main__':
    parse_candidates_html()
