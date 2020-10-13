%%time
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

#get links

http = httplib2.Http()
status, response = http.request('http://www.upes.ac.in')
links=[]
for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        links.append(link.get('href'))

#Links from all links
 
count=0
links=list(set(links))
links1=links
for x in range(0,len(links1)):
    try:
      req = Request(links1[x])
      html_page = urlopen(req)
      soup = BeautifulSoup(html_page)
      #print(x)
      #count=count+1
      #print(links1[x])
      for link in soup.findAll('a'):
        links.append(link.get('href'))
    except:
        pass
