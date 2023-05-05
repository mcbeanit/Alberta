Set-ExecutionPolicy -Scope CurrentUser ByPass

scrapy runspider ab_parties_spider.py --nolog
scrapy runspider gpa_candidates_spider.py --nolog
scrapy runspider ndp_candidates_spider.py --nolog
scrapy runspider ucp_candidates_spider.py --nolog

python ap_parties.py



