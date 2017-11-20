import mechanize
from bs4 import BeautifulSoup
import sys

offerSite = 'https://www32.uac.edu.au/offers'
br = mechanize.Browser()
#applicationNum = ""
#pin = ""

def fileRead():

        try:
                infoFile = open('cred.txt')
        
                global applicationNum
                applicationNum = str(infoFile.readline())
                global pin
                pin = str(infoFile.readline())

                infoFile.close()
        except:
                print 'Cannot open file "cred.txt"'
                sys.exit(1)

def mainBrowsing():
        fileRead()
        try:
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

        except:
                print sys.exc_info()[0]
                print 'Cannot read the website\n'
                print 'Make sure all your credentials are put correct' 
                sys.exit(1)

	try:
		infoFile = open('cred.txt')
	
		global applicationNum
		applicationNum = str(infoFile.readline())
		global pin
		pin = str(infoFile.readline())

		infoFile.close()
	except:
		print 'Cannot open file "cred.txt"'
		sys.exit(1)

def mainBrowsing():
	fileRead()
	try:
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

	except:
		print 'Cannot read the website\n'
		print 'Make sure all your credentials are put correct' 
		sys.exit(1)

mainBrowsing()
