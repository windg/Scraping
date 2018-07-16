
from bs4 import BeautifulSoup as soup

import requests

url = 'https://docs.google.com/spreadsheets/d/1I4OR0gkRo6u62tKYSPgotVhg5-SQMDZ2v1fidqsCvBw/edit#gid=0'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
pageHtml = requests.get(url, headers=headers)

# Get the page


pageSoup = soup(pageHtml.text,"html.parser")
containers = pageSoup.findAll("div",{"class":"item-container"})
