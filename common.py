from bs4 import BeautifulSoup
from urllib.request import urlopen

def extract(uri):
    '''take an href tag and extract only the link'''

    start = uri.find("\"")     # find first occurrence of "
    ends = uri.find("\"", start+1)   # find the next occurrence of  "

    return uri[start+1:ends]

def openReturnBS(url):
    return None

def trimBio(bio):
    '''trim the "..." and html tags from the text'''

    return bio
