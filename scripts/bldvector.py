#! C:\python27
#-*- coding: utf-8 -*-
import re, urllib, urllib2, pymongo, datetime
import numpy as np
from pymongo import MongoClient
class VecBuilder:
	def Build(self):
		print "Building Vectors"
		client=self.CreateConnection()
		db=client.meteor
		try:
			cursor_d = db.dictionary.find()
		except:
			print "Can't download dictionary from database."
		try:
			cursor_wp = db.webpages.find()
		except:
			print "Can't download webpages from database."
		dictionary = self.GetWords(cursor_d)
		self.BuildVectors(cursor_wp, db, dictionary)
		print "Vectors updated."

	def CreateConnection(self):
		try:
			return MongoClient('mongodb://127.0.0.1:3001/meteor')
		except:
			print "ERROR: Can't connect to database."

	def GetWords(self, cursor_d):
		dictionary = []
		for obj in cursor_d:
			dictionary.append(obj.get('word').encode("utf8"))
		return dictionary

	def BuildVectors(self, cursor_wp, db, dictionary):
		vector = []
		for webpage in cursor_wp:
			if not webpage.get('vector'):
				del vector[:]
				vector[:] = []
				cursor_d = db.dictionary.find()
				text = webpage.get('html_strip').encode("utf8")
				for obj in dictionary:
					vector.append(text.count(obj))
				db.webpages.update_one({ "_id": webpage.get("_id")}, { '$push': {'vector' : {'$each':vector}} })
