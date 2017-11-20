# uacOfferChecker
This thing automatically checks your offers from the uac website for undergraduates

Requirements
-----------

requires python 2.x to work python 3.x won't.
Preferred choice is python 2.7 as the system was built in it.

Topic
----

Tired of logging everytime into the UAC(University admissions Centre) website to check you undergraduate offers?
This thing does it for you automatically

Usage
----

Just paste your application ID and your pin on the first and second line of the 'cred.txt' file and then just run the app to recieve your offer


How it works
-----------

It basically just uses mechanize and beautifulsoup4 in the inside to automate the login and finally gives out the output to you

Installation
-----------

Just goto to the uacChecker folder and then run :
"python setup.py develop" to install all the dependencies.
Dependencies wont install if its not python 2.x.

For linux: 	Run linuxRunner.sh file with proper credentials in the cred.txt file

For windows: Just double click on windowsRunner.bat with proper credentials on cred.txt file.

Bugs
----

- The thing may not work if the uac offer website is changed.
- You'll get all bugged up output if your application number or pin is incorrect
