Set-ExecutionPolicy -Scope CurrentUser ByPass

# scrapers using the scrapy application get the relevant html and save
# it to various html files.
scrapy runspider ab_parties_spider.py --nolog
scrapy runspider ab_ridings_spider.py --nolog

scrapy runspider alp_candidates_spider.py --nolog
scrapy runspider alp_candidates_spider_more.py --nolog

scrapy runspider ap_candidates_spider.py --nolog
scrapy runspider apghgh_candidates_spider_more.py --nolog

scrapy runspider gpa_candidates_spider.py --nolog
scrapy runspider gpa_candidates_spider_more.py --nolog

scrapy runspider ndp_candidates_spider.py --nolog
scrapy runspider ndp_candidates_spider_more.py --nolog

scrapy runspider ucp_candidates_spider.py --nolog
scrapy runspider ucp_candidates_spider_more.py --nolog

scrapy runspider official_candidates_spider.py --nolog

# scripts to extract data of interest from the htnl saved by the crawler
# and create the csv files.

python ab_parties.py

python alp_candidates.py
pythin alp_candidates_more.py

python ap_candidates.py
python ap_candidates_more.py

python gpa_candidates.py
python gpa_candidates_more.py

python ndp_candidates.py
python ndp_candidates_social.py

python ucp_candidates.py

python official_candidates.py





