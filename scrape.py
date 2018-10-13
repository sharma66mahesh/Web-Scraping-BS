from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from common import extract, openReturnBS, trimBio

actorName = input("Enter actor name to find").strip()

actorName = actorName.replace(" ", "+")

# we extract the actual actor's url (finalUrl) from this url below
url = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + actorName + "&s=all"

urlClient = urlopen(url)    # a file-like object is returned
urlContent = urlClient.read()
urlClient.close()

# print(urlContent)
pageSoup = BeautifulSoup(urlContent, "html.parser") # a beautifulSoup object. Now can access the html pages's tags as pageSoup.h1, etc
str = str(pageSoup.find("table", {"class":"findList"}))  # findAll returns a list. find returns first element

uri = re.findall(r'<a href="\/name[^>]*>', str)[0]

finalUrl = "http://imdb.com" + extract(uri)

urlClient = urlopen(finalUrl)    # a file-like object is returned
urlContent = urlClient.read()
urlClient.close()

pageSoup = BeautifulSoup(urlContent, "html.parser")
bio = pageSoup.find("div", {"class":"name-trivia-bio-text"}).div
print(trimBio(bio))
