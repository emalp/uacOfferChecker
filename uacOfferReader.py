import mechanize
from bs4 import BeautifulSoup


offerSite = 'https://www32.uac.edu.au/offers'
br = mechanize.Browser()
applicationNum = ""
pin = ""


def mainBrowsing():
	br.open(offerSite)

	br.select_form(nr=0)
	

	br.form['refNum'] = applicationNum # the uac number
	br.form['pin'] = pin # the uac pin

	br.submit()

	# eveything's done, now print the output to the user in nice format

	soup = BeautifulSoup(br.response().read(), 'lxml')

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



infoFile = open('cred.txt')
	
applicationNum = str(infoFile.readline())
pin = str(infoFile.readline())

infoFile.close()

mainBrowsing()
