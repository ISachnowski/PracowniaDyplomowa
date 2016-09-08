#! C:\python27
#-*- coding: utf-8 -*-
import re, urllib, urllib2, pymongo, datetime
import numpy as np
from pymongo import MongoClient
class DicBuilder:

	def CreateConnection(self):
		try:
			return MongoClient('mongodb://127.0.0.1:3001/meteor')
		except:
			print "ERROR: Can't connect to database."


	def CountWords(self,webpages, db):
		wordcount={}
		for wp in webpages:
			for word in wp.get('html_strip').split():
				if word not in wordcount:
					wordcount[word] = 1
				else:
					wordcount[word] +=1
			try:
				db.webpages.update_one({ "_id": wp.get("_id")},
					   { "$set": { "status": "Scanned"} })
			except:
				print "ERROR: Can't update webpage in database."
		return wordcount

	def UpdateDictionaryToDB(self,wordcount, db):
		for k,v in wordcount.items():
			item = {"word" : k,  "count" : v}
			try:
				db.dictionary.insert_one(item)
			except:
				print "ERROR: Can't insert word into dictionary."
		print len(wordcount)

	def Build(self):
		print "Creating Dictionary..."
		client=self.CreateConnection()
		db=client.meteor
		webpages=db.webpages.find()
		wordcount = self.CountWords(webpages,db)
		self.UpdateDictionaryToDB(wordcount,db)
		print "Dictionary Created."

		


		









