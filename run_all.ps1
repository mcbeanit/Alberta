Set-ExecutionPolicy -Scope CurrentUser ByPass

scrapy runspider ab_parties_spider.py --nolog
scrapy runspider alp_candidates_spider.py --nolog
scrapy runspider ap_candidates_spider.py --nolog
scrapy runspider gpa_candidates_spider.py --nolog
scrapy runspider ndp_candidates_spider.py --nolog
scrapy runspider official_candidates_spider.py --nolog
scrapy runspider ucp_candidates_spider.py --nolog

python ab_parties.py
python alp_candidates.py
python ap_candidates.py
python gpa_candidates.py
python ndp_candidates.py
python official_candidates.py
python ucp_candidates.py




