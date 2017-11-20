from setuptools import setup

setup(
	name = "uacChecker",
	version = '1.0',
	desciption = 'Checks for your UAC undergraduate offers',
	author = 'emalp',
	install_requires = ['mechanize', 'bs4', 'lxml'],
	zip_safe = False
	)

