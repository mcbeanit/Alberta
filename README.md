# Alberta
Alberta election 2023 data sets

Using scrapy to extract dataset from varous sources, and further processing
to validate and import the data into Excel. 

The link to the spreadsheet on office.com(view only for now):
    https://1drv.ms/x/s!AjxE0-lM49G1g9EtCYTVfl4KcErOyw?e=vW0vr4

Completed:
    Basic list of Alberta Ridings and current MLA.

Working on:
    List of official parties.

Future:
    Candidate list.


Files in project:

* *ab_parties_spider.py*        Runs the scrapy spider to get the parties from Election Alberta.
* *ab_parties.csv*              validated csv listing the official parties.
* *ab_parties.html*             the extracted HTML of interest to produce the csv file
* *ab_ridings.spider.py*        Runs the scrapy spider to get the list of ridings from Wikipedia
* *ab_ridings.csv*              Validated csv listing of alberta ridings.
* *main.py*                     Entry point to run the import scrips(s).
* *ab_ridings.html*             Extracted HTML of interest to produce the csv file.  

How to run (so far)

`scrapy runspider ab_ridings_spider.py`

`scrapy runspider ab_parties_spider.py`

`python main.py`               
