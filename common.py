from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def extract(uri):
    '''take an href tag and extract only the link'''

    start = uri.find("\"")     # find first occurrence of "
    ends = uri.find("\"", start+1)   # find the next occurrence of  "

    return uri[start+1:ends]

def openBS(url):
	'''open url and return BeautifulSoap object contatining the content of the url'''
	urlClient = urlopen(url)    # a file-like object is returned
	urlContent = urlClient.read()
	urlClient.close()

	# a beautifulSoup object. Now can access the html pages's tags as pageSoup.h1, etc
	pageSoup = BeautifulSoup(urlContent, "html.parser")
	return pageSoup

def trimBio(bio):
    '''trim the "..." and html tags from the text'''
    finalIndex = bio.find("...")

    bio = bio[:finalIndex]

    tags = re.findall(r'<[^>]+>', bio)	# find all the tags in the string

    for tag in tags:
    	bio = bio.replace(tag, "")

    return bio
