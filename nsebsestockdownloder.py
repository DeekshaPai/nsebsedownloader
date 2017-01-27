""" downloads the individual stock file from yahoo and saves it in a different directory """

"""to do - download the files in parallel using threads and parallel processing """

import urllib
import os

def converttostockindices():
	f=open("result.csv","r")
	readchar=f.read()
	listval =[]
	listval=readchar.split()[2:]
	return listval

def bsedownloader(string):
	testfile = urllib.URLopener()
	directory="./testfilesBO"
	os.makedirs(directory)
	for url in string:
		new_url="http://real-chart.finance.yahoo.com/table.csv?s="+url+".BO&d=0&e=27&f=2017&g=d&a=0&b=3&c=2000&ignore=.csv"
		#print new_url
		#dir = os.path.dirname(__file__)
		fullfilename = os.path.join("./testfilesBO",url+".csv")
		testfile.retrieve(new_url,fullfilename)
		print "saved file - %s" %(url)

def nsedownloader(string):
	testfile = urllib.URLopener()
	directory="./testfilesNS"
	os.makedirs(directory)
	for url in string:
		new_url="http://real-chart.finance.yahoo.com/table.csv?s="+url+".NS&d=0&e=27&f=2017&g=d&a=0&b=3&c=2000&ignore=.csv"
		#print new_url
		#dir = os.path.dirname(__file__)
		try:
			fullfilename = os.path.join("./testfilesNS",url+".csv")
			testfile.retrieve(new_url,fullfilename)
			print "saved file - %s" %(url)
		except:
			pass

string=converttostockindices()
nsedownloader(string)
#bsedownloader(string)  enable to download bse aswell 

print "done"






