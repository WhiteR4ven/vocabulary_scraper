#!/usr/bin/env python3

#packages to install:
# pip install soupsieve
# pip install beautifulsoup4
# pip install bs4
# pip install dnspython
# pip install pymongo

import requests  # lib to make web requests
from bs4 import BeautifulSoup

# read in url-list
 with open('vocab_input.txt') as vocab_input:
    vocab_search = []
    vocab_search = [line.rstrip() for line in vocab_input]

    # create empty data list
    data = []

  # loop through vocab input
  for i in vocab_search:
    #print(i)
    url = "https://cooljugator.com/ro/" + i
    print(url)
  
# download content from the web url

# scrape the online data
      
# save Data to output.txt
    
# EOF
