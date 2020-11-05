from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.upes.ac.in/"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)



from pymongo import MongoClient
from random import randint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db=client.test1
textspl=text.split()
for x in textspl:
    business = {
        'text' : x.lower(),
        'docid' : 1
    }
    #Step 2: Insert business object directly into MongoDB via isnert_one
    result=db.index.insert_one(business)
#Step 3: Tell us that you are done
print('finished indexing')
