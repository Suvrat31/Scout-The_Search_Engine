%%time
import urllib.request as ur
import lxml.html
links=[]

#gets links

connection = ur.urlopen('http://www.upes.ac.in')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    links.append(link)

#2nd Degree links

count=0
links=list(set(links))
links1=links
for x in range(0,len(links1)):
  try:
    connection = ur.urlopen(links1[x])
    dom =  lxml.html.fromstring(connection.read())
    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
      links.append(link)
  except:
    pass
