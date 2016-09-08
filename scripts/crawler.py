#! C:\python27
#-*- coding: utf-8 -*-
import re, urllib, urllib2, pymongo, datetime, lxml
import numpy as np
from lxml.html.clean import Cleaner
from pymongo import MongoClient
cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True
def remove_html_markup(s):
	tag = False
	quote = False
	out = ""
	for c in s:
		if c == '<' and not quote:
			tag = True
		elif c == '>' and not quote:
			tag = False
		elif (c == '"' or c == "'") and tag:
			quote = not quote
		elif not tag:
			out = out + c
	return out

class Crawler:
	def Run(self):
		print "Crawling..."
		
		client=self.CreateConnection()
		db=client.meteor
		webpages=db.webpages.find()
		for webpage in webpages:
			myurl = webpage.get('url')
			self.Crawl(myurl,db)
			

	def CreateConnection(self):
		try:
			return MongoClient('mongodb://127.0.0.1:3001/meteor')
		except:
			print "ERROR: Can't connect to database."

	def Crawl(self,myurl,db):
		now = datetime.datetime.now()
		urllist = []
		for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
				if i.find("http://") == -1 and i.find("https://") == -1:
					i=myurl+i;
				try:
					for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
						if ee.find("http://") == -1 and ee.find("https://") == -1:
							ee=myurl+ee
							print ee
						if (ee in urllist) == False:
							urllist.append(ee)
							response = urllib2.urlopen(ee)
							page_source = response.read()
							page_source = ' '.join(page_source.split())
							page_source_strip = cleaner.clean_html(page_source)
							page_source_strip = remove_html_markup(page_source_strip)
							page_source_strip = ''.join(c for c in page_source_strip if c not in ',:"1234567890().[]{};!@#$%^&*-_=+/?')
							webpage = {"url" : ee,  "html_strip" : 	page_source_strip, "last_update" : now, "status" : "Created", "vector" : [] }
							try:
								db.webpages.insert_one(webpage)
							except:
								print "Can't insert webpage into database."
				except Exception:
					pass
