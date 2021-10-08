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
try:
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

    # note search vocab to output data list
    data.append("\n") # insert newline to sepratate single vocabs
    data.append(i)
    data.append("\t") # insert a tab

    # download content from the web url
    try:
      html = requests.get(url)
      soup = BeautifulSoup(html.content, "html.parser")
      
      search = ["present1", "present2", "present3", "present4", "present5", "present6"]
      
      # scrape the online data
      for j in search:
        conjug = soup.find(id=j).find(class_="forms-wrapper").find(class_="meta-form").text
        #print(conjug)
        data.append(conjug) # append to existing data
        data.append("\t") # insert a tab
         
    except:
      print('error: No online data found')
    
  # save Data to output.txt
    vocab_output = open('vocab_output.txt','w')
    
    for x in range(len(data)):
      #print(data[x])
      vocab_output.write(data[x])

    vocab_output.close()

except IOError:
  print('error: Vocab Input file does not exist')

# EOF
