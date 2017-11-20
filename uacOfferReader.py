import mechanize
from bs4 import BeautifulSoup
import sys

offerSite = 'https://www32.uac.edu.au/offers'
br = mechanize.Browser()
applicationNum = ""
pin = ""

def mainBrowsing():
	try:
		br.open(offerSite)

		br.select_form(nr=0)	

		br.form['refNum'] = applicationNum # the uac number
		br.form['pin'] = pin # the uac pin

		br.submit()

	# eveything's done, now print the output to the user in nice format

		soup = BeautifulSoup(br.response().read(), 'lxml')
	except err: 
		print "Can't get to the website!"
		sys.exit(1)

	offerData = soup.find_all('p')
	
	print offerData[0]
	print '\n' 
	print offerData[1]
	print '\n' 
	print offerData[2]
	print '\n' 
	print offerData[3]
	print '\n' 
	print offerData[4]

try:
	infoFile = open('cred.txt')
	
	applicationNum = str(infoFile.readline())
	pin = str(infoFile.readline())

	infoFile.close()
except filerr:
	print 'Cannot open file "cred.txt"'
	sys.exit(1)

mainBrowsing()
