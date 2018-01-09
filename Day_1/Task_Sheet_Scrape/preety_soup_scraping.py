import urllib
#import pymongo
import json
from urllib import urlopen
#y = "https://news.ycombinator.com/jobs"
y = "https://www.androidauthority.com/android-8-0-review-758783/"
page = urlopen(y)

from bs4 import BeautifulSoup

data={}
data['jobs']=[]

soup=BeautifulSoup(page,"lxml")
all_links=soup.find_all("a",class_="storylink")
for x in all_links :
 data['jobs'].append({'title':x.string,'link':x.get("href")})

with open('data.json', 'w') as outfile:  
   json.dump(data, outfile)