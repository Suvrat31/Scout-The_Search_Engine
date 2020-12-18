import urllib.request as ur
import lxml.html
from threading import Thread
from queue import Queue
import jaydebeapi
import jaydebeapi
conn = jaydebeapi.connect("org.h2.Driver", # driver class
                            "jdbc:h2:tcp://localhost/~/test", # JDBC url
                            ["sa", ""], # credentials
                            r"/home/sumer/Desktop/Hmm/Major/Search/Sandbox/h2-1.4.200.jar",) # location of H2 jar


links = Queue()

def producer():
    connection = ur.urlopen('http://www.upes.ac.in')
    dom =  lxml.html.fromstring(connection.read())
    links1=[]
    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
        links1.append(link)

#2nd Degree links

    links1=list(set(links1))
    for x in range(0,len(links1)):
        try:
            connection = ur.urlopen(links1[x])
            dom =  lxml.html.fromstring(connection.read())
            for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
                links.put(link)
        except:
            pass


def consumer():
    try:
        curs = conn.cursor()
        while True:
            linkstr = links.get()
            query="select * from links where link='"+linkstr+"'"
            curs.execute(query)
            results=curs.fetchall()
            if(len(results)==0):
                query="INSERT INTO links (link, count,tokeniszed)VALUES ('"+linkstr+"', 1,0);"
                curs.execute(query)
            else:
                query="UPDATE links SET count = count + 1 where link='"+linkstr+"'"
                curs.execute(query)
            links.task_done()
    finally:
        if curs is not None:
                curs.close()
        if conn is not None:
                conn.close()
t = Thread(target=consumer)
t.daemon = True
t.start()

producer()
