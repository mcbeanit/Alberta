Set-ExecutionPolicy -Scope CurrentUser ByPass

# scrapers using the scrapy application get the relevant html and save
# it to various html files.
scrapy runspider ab_parties_spider.py --nolog
scrapy runspider pyth --nolog

scrapy runspider alp_candidates_spider.py --nolog
scrapy runspider alp_candidates_spider_more.py --nolog

scrapy runspider ap_candidates_spider.py --nolog
scrapy runspider ap_candidates_spider_more.py --nolog

scrapy runspider gpa_candidates_spider.py --nolog
scrapy runspider gpa_candidates_spider_more.py --nolog

scrapy runspider ndp_candidates_spider.py --nolog
scrapy runspider ndp_candidates_spider_more.py --nolog

scrapy runspider ucp_candidates_spider.py --nolog
scrapy runspider ucp_candidates_spider_more.py --nolog

scrapy runspider official_candidates_spider.py --nolog

# scripts to extract data of interest from the html saved by the crawler
# and create the csv files.

python ab_parties.py

python alp_candidates.py
python alp_candidates_more.py

python ap_candidates.py
python ap_candidates_more.py

python gpa_candidates.py
python gpa_candidates_more.py
python gpa_candidates_social.py

python ndp_candidates.py
python ndp_candidates_social.py

python ucp_candidates.py
python ucp_candidates_social.py

python official_candidates.py





