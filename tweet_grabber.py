import urllib
from bs4 import BeautifulSoup as soup
import re

html = urllib.urlopen('https://twitter.com/<account>').read()
bs = soup(html)
x = bs.find("meta", {"name":"description"})['content']
print x
filter = re.findall(r'"(.*?)"', x)
tweet = filter[0]
print tweet

