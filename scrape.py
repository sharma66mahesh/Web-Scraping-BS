from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from common import extract, openBS, trimBio

actorName = input("Enter actor name to find:\t").strip()

actorName = actorName.replace(" ", "+")

# we extract the actual actor's url (finalUrl) from this url below
url = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + actorName + "&s=all"

pageSoup = openBS(url)
strng = str(pageSoup.find("table", {"class":"findList"}))  # findAll returns a list. find returns first element

uri = re.findall(r'<a href="\/name[^>]*>', strng)[0]

finalUrl = "http://imdb.com" + extract(uri)

pageSoup = openBS(finalUrl)

bio = str(pageSoup.find("div", {"class":"name-trivia-bio-text"}).div)
print(trimBio(bio))
