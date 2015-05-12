import urllib2
import re
import codecs

from bs4 import BeautifulSoup
outputfile = codecs.open("output.txt", "w", "utf-8")

inputfile = codecs.open("big.html", "r", "utf-8")

soup = BeautifulSoup(inputfile)
soup.encode('utf-8')

paragraphs = soup.find_all('span')
for p in paragraphs:
	if p.string != 'None' and p.string != ' · ':
		print unicode(p.string)
		outputfile.write( unicode(p.string) )
		outputfile.write('\n')
