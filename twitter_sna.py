#!/usr/bin/python

import os
import sys
import couchdb
from couchdb.design import ViewDefinition


tagTwo ="justinbieber"
tagOne = "oslo"


def collectUsersFromSearch(db_name = 'search-' + tagOne):


	DB = db_name

	try:
		server = couchdb.Server('http://localhost:5984')
		db = server[DB]
	except couchdb.http.ResourceNotFound, e:
		print """CouchDB database '%s' not found. 
	Please check that the database exists and try again.""" % DB
		sys.exit(1)

	def screenNameMapper(doc):
		if doc.get('from_user'):
			yield (doc.get('from_user'), [doc['_id'], doc['id']])
	
	def dummyReducer(keys, values):
		return True

	view = ViewDefinition('index', 'screen_names', screenNameMapper, reduce_fun=dummyReducer, language='python')
	view.sync(db)

	for row in db.view('index/screen_names', group = True):
		# we need to crawl those users	
		print ('python sna_twitter/friends_followers__get_user_info.py ' + row.key)
		os.system('python sna_twitter/friends_followers__get_user_info.py ' + row.key)

if __name__ == '__main__':
	print ('python sna_twitter/the_tweet__search.py ' + tagOne)
	# os.system('python sna_twitter/the_tweet__search.py ' + tagOne)
	collectUsersFromSearch('search-'+tagOne)
#	os.system('python sna_twitter/friends_followers__redis_to_networkx_ymir.py')

	
