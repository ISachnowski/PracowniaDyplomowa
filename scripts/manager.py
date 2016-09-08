#! C:\python27
#-*- coding: utf-8 -*-
import re, urllib, urllib2, pymongo, datetime
import numpy as np
from crawler import Crawler
from bldvector import VecBuilder
from bldmodel import BuildModel
from dictionary import DicBuilder
from pymongo import MongoClient
client=MongoClient('mongodb://127.0.0.1:3001/meteor')
db=client.meteor

Dictionary = DicBuilder()
crawler = Crawler()
vectorBuilder = VecBuilder()
bldModel = BuildModel()
cursor_wp = db.webpages.find()

crawler.Run()
Dictionary.Build()
vectorBuilder.Build()
bldModel.Build()

cursor_wp = db.webpages.find()
for webpage in cursor_wp:
	if not webpage.get('category'):
		category = bldModel.PredictCategory(webpage.get('vector'))
		db.webpages.update_one({ "_id": webpage.get("_id")}, 
					{ '$push': {'category' : category} })

