# Alberta
Alberta election 2023 data sets

Using scrapy to extract dataset from varous sources, and further processing
to validate and import the data into Excel. 

The link to the spreadsheet on office.com(view only for now):
    https://1drv.ms/x/s!AjxE0-lM49G1g9EtCYTVfl4KcErOyw?e=vW0vr4

Completed:
    Basic list of Alberta Ridings and current MLA.
    Candidate list for NDP, UCP, ALP, AGP,

## Working on:
    Bios of candidates if they are available.
    Demographics of candidates.
    Master list of candidates (in Excel)
    Clean up messy code

## Future:
    Master list of official candidates from Elections Alberta
    

## Notes on file names and conventions
* Files ending in py are python scripts that can just be run from a command line
* Python files with "spider" in their name are using Scrapy to extract html.
* CSV files are tab delimited, and right now we are not using column name headers

## Files in project:

* *ab_candidates.csv*           Master list of candidates
* *ab_nominated_counts.csv      Summary count of nominees by party and gender

* *ab_parties_spider.py*        Runs the scrapy spider to get the parties from Election Alberta.
* *ab_parties.csv*              validated csv listing the official parties.
* *ab_parties.html*             the extracted HTML of interest to produce the csv file
* *ab_parties.py*               product the list of parties

* *ab_ridings.spider.py*        Runs the scrapy spider to get the list of ridings from Wikipedia
* *ab_ridings.csv*              Validated csv listing of alberta ridings.
* *ab_ridings.html*             Extracted HTML of interest to produce the csv file.  

* *alp_candidates_spider_more.py*   Alberta Liberal Party candidate bios.
* *alp_candidates_spider.py*    Alberta Liberal Party list of candidates(html)
* *alp_candidates.csv*          Alberta Liberal Party list of candidates(csv)
* *alp_candidates,html*         Relevant html found by scrapy
* *alp_candidates.py*           Product csv list from html

* *ap_candidates_spider.py*     Alberta Party scrapy to get relevant html
* *ap_candidates.csv*           Alberta Party list of candidates
* *ap_candidates.py*            Produce the csv list of candidates

* *gender_guesser.py*           Try to guess a person's gender if you don't know

* *gpa_candidates_spider.py*    Get the relevant candidate html with scrapy 
* *gpa_candidates.csv*          Green Party of Alberta List of Candidates
* *gpa_candidates.py            Green Party of Alberta create the csv from html

* *ndp_candidates_more.csv*     NDP candidates bios and sm links
* *ndp_candidates_spider_more.py*    Scrapy follow candidate links into bio and extract html
* *ndp_candidates_spider.py*    NDP Candidates extract relevant html.
* *ndp_candidates_csv*          NDP Candidates list.
* *ndp_candidates.html*         NDP candidates list extracted html
* *ndp_candidates.py*           NDP candidates read html and produce csv

* *run_all.ps1*                 PowerShell script to run all the scripts
* *settings.json*               Stores some application settings. (Not much use right now)

* *test_ab_parties.py*          PyTest test suite
* *test_ucp_candidates.py*      PYTest test suite

* *ucp_candidates_spider_more.py*    UCP Candidates bios with scrapy.
* *ucp_candidates_spider.py*    UCP Candidates basic list with scrapy.
* *ucp_candidates.csv*          UCP list of candidates.
* *ucp_candidates.html*         UCP extracted html list of candidates
* *ucp_candidates.py*           UCP read html and produce the csv

* *ucp_mlas.csv*                UCP MLAs from their list
* *ucp_mlas.html*               UCP MLAs extracted html
* *ucp_not_running.csv*         List of UCP MLAs not running again.



    


How to run (typical example)

`scrapy runspider ab_ridings_spider.py`
`python ab_ridings.py`

          
