%%time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pymongo import MongoClient
from random import randint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db=client.token
import jaydebeapi
conn = jaydebeapi.connect("org.h2.Driver", # driver class
                            "jdbc:h2:tcp://localhost/~/test", # JDBC url
                            ["sa", ""], # credentials
                            r"/home/sumer/Desktop/Hmm/Major/Search/Sandbox/h2-1.4.200.jar",) # location of H2 jar

try:
    curs = conn.cursor()
    query="select * from links where tokeniszed=0"
    curs.execute(query)
    results=curs.fetchall()
    query=0
    
    for link_info in results:

        url = link_info[1]
        try:
            html = urlopen(url).read()


            temp_var=[]
            temp_var.append(link_info[0])
            temp_var.append(link_info[1])
            temp_var.append(link_info[2])
            soup = BeautifulSoup(html, features="html.parser")

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out

            # get text
            text = (soup.get_text()).lower()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)

            text=text.split()

            words={}
            for index in range(0,len(text)):
                if(text[index] in words):
                    words[text[index]][1]=words[text[index]][1]+1
                else:
                    words[text[index]]=[index,1]

            for x in words:
                temp_var1=temp_var+words[x]
                document = {
                    'word' : x,
                    'docid' : [temp_var1]
                }
                #Step 2: Insert business object directly into MongoDB via isnert_one

                results=db.words.update({'word': x}, {'$push': {'docid': temp_var1}})
                if(results['n']==0):
                    result=db.words.insert_one(document)
                query="UPDATE links SET tokeniszed = 1 where link='"+link_info[1]+"'"
                curs.execute(query)
                temp_var1=[]

            #Step 3: Tell us that you are done
            #print('finished indexing')
        except:
            pass

finally:
    if curs is not None:
        curs.close()
    if conn is not None:
        conn.close()
