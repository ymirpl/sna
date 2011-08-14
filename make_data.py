#import os
import sys
import couchdb
from couchdb.design import ViewDefinition
import redis, twitter
import networkx as nx
#import matplotlib.pyplot as plt
import pickle
#import json
import random
from sna_twitter.twitter__util import makeTwitterRequest
import prettytable


tagOne = "justinbieber"
tagTwo = "teaParty"

r = redis.Redis()

TAG = 'justin'
TAGLONG = 'justinbieber'


def readGPickle(path = './out/'  + TAG + '-ids.gpickle'):
	graph = nx.read_gpickle(path)

	return graph

def draw():
	# TODO: don't show labels
	nx.draw(G)
	plt.show()

def computeClusteringCoeff(g):
	cc = nx.average_clustering(g)
	print cc
	pickle.dump(cc, open( "./out/" + TAG + "-clustering-coefficient.pickle", "wb"))

def degreeDist(g):
	print g.number_of_nodes()

	dd = dict()

	nodesDegs = g.degree(g.nodes())

        print nodesDegs

	for deg in nodesDegs.values():
		if deg in dd:
			dd[deg] += 1
		else:
			dd[deg] = 1
	
	print sorted(dd)

	pickle.dump(dd, open( "./out/" + TAG + "-degree-dist-dict.pickle", "wb"))

def computeRetweets(db_name = 'search-' + TAGLONG):


	fraction = 0.65
	DB = db_name
	db_write = db_name + '-full'

	try:
		server = couchdb.Server('http://localhost:5984')
		db = server[DB]
	except couchdb.http.ResourceNotFound, e:
		print """CouchDB database '%s' not found. 
	Please check that the database exists and try again.""" % DB
		sys.exit(1)
	
	try:
		db = server.create(db_write)
	except couchdb.http.PreconditionFailed, e:
		db_write = server[db_write]

	def idMapper(doc):
		yield (doc['id'], [doc['_id'], doc['id']])
	
	def dummyReducer(keys, values):
		return True

	view = ViewDefinition('index', 'ids', idMapper, reduce_fun=dummyReducer, language='python')
	view.sync(db)

	t = twitter.Twitter(domain='api.twitter.com', api_version='1')
	api_call = getattr(t.statuses, 'show')
	tcounter = 0
	rtCounter = dict()

	for row in db.view('index/ids', group=True):
		if random.random() < fraction:
			print "Fetching tweet ", row.key
			try:
				tweet = makeTwitterRequest(t, api_call, id=row.key)
			except:
				print "Some kind of exception, passing"
				continue
				
#			db_write.update(tweet, all_or_nothing=True)

			if tweet == None:
				continue

			rc = tweet.get('retweet_count')
			print "Got retweet count ", rc
			if rc in rtCounter:
				rtCounter[rc] += 1
			else:
				rtCounter[rc] = 1
			
			tcounter += 1
		else:
			pass



	pickle.dump(rtCounter, open( "./out/"+TAG+"-rtcount-dist-dict.pickle", "wb"))
	print rtCounter
	print "Fetched ", tcounter, " tweets"


	

def computeRetweetsDist(db_name = 'search-' + TAGLONG):
	try:
		server = couchdb.Server('http://localhost:5984')
		db = server[db_name]
	except couchdb.http.ResourceNotFound, e:
		print """CouchDB database '%s' not found. Please check that the database exists and try again.""" % DB
		sys.exit(1)


	def retweetCountMapper(doc):
		if doc.get('text'):
			import re
			m = re.search(r"(RT|via)((?:\b\W*@\w+)+)", doc['text'])
			if m:
				entities = m.groups()[1].split()
			for entity in entities:
				yield (entity.lower(), [doc['_id'], doc['id']])
		elif doc.get('retweeted_status'):
			entity = doc.get('retweeted_status').get('user').get('screen_name')
			yield (entity.lower(), [doc['_id'], doc['id']])
		else:
			yield ('@', [doc['_id'], doc['id']])

	def summingReducer(keys, values, rereduce):
		return sum(values)

	view = ViewDefinition('index', 'retweets_by_id', retweetCountMapper, 
						  reduce_fun=summingReducer, language='python')

	view.sync(db)

	fields = ['Retweet Count', 'Num Tweets']
	pt = prettytable.PrettyTable(fields=fields)
	[pt.set_field_align(f, 'l') for f in fields]

	retweet_total, num_tweets, num_zero_retweets = 0, 0, 0
	for (k,v) in sorted([(row.key, row.value) for row in 
						 db.view('index/retweets_by_id', group=True)
						 if row.key is not None],
					 key=lambda x: x[0], reverse=True):
		pt.add_row([k, v])


def computeCentrality(g):
	cty = dict()
	cty['degree'] = nx.algorithms.centrality.degree_centrality(g)
	cty['betweenness'] = nx.algorithms.centrality.betweenness_centrality(g)
	cty['closeness'] = nx.algorithms.centrality.closeness_centrality(g)
	cty['eigenvector'] = nx.algorithms.centrality.eigenvector_centrality(g)

	pickle.dump(cty, open( "./out/"+TAG+"-cty-dict.pickle", "wb"))


def basicMarks(g):
	print "No node, no edges"
	print g.number_of_nodes(), g.number_of_edges()
 
def avgShortestPath(g):
    l = nx.connected_components(g)[0]

    # delete all but component

    for node in g.nodes():
        if node not in l:
            g.remove_node(node)


    print "Largest connected component %d %d" % (g.number_of_nodes(), g.number_of_edges())
    print "Avg shortest path for graph " + tagOne
    print(nx.average_shortest_path_length(g))


def avgClusteringCoeff(g):
    print "Avg clustering for graph " + tagOne
    print(nx.average_clustering(g))


if __name__ == "__main__":
	G = readGPickle()
        avgClusteringCoeff(G)
        avgShortestPath(G)
#       basicMarks(G)
#	degreeDist(G)
#	computeCentrality(G)
#	computeClusteringCoeff(G)
#	computeRetweets()
