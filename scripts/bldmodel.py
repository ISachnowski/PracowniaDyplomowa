#! C:\python27
#-*- coding: utf-8 -*-
import re, urllib, urllib2, pymongo, datetime
from sklearn import svm
from pymongo import MongoClient
class BuildModel:
	def Build(self):
		print "Buiding Model"
		client=self.CreateConnection()
		db=client.meteor
		try:
			cursor_wp = db.webpages.find()
		except:
			print "Can't download webpages from database."
		X = []
		y = []
		for webpage in cursor_wp:
			if webpage.get('category'):
				X.append(webpage.get('vector'))
				y.append(webpage.get('category'))
		try:
			clf = svm.SVC()
			clf.fit(X,y)
		except:
			print "Can't build a model."

	def PredictCategory(vector,self):
		return clf.predict(vector)
	
	def CreateConnection(self):
		try:
			return MongoClient('mongodb://127.0.0.1:3001/meteor')
		except:
			print "ERROR: Can't connect to database."
