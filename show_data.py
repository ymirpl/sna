import os
import sys
import couchdb
from couchdb.design import ViewDefinition
import redis, twitter
import networkx as nx
#import matplotlib.pyplot as plt
import pickle
import json
import random
from sna_twitter.twitter__util import makeTwitterRequest


tagOne = "oslo"
tagTwo = "teaParty"

r = redis.Redis()

TAG = 'justin'
TAGLONG = 'oslo'


def readGPickle(path = './out/'  + TAG + '-ids.gpickle'):
	graph = nx.read_gpickle(path)

	return graph

def draw(G):
	nx.draw(G, with_labels = False)
	plt.show()



def degreeDist():
	dd = pickle.load(open( "./out/"+TAG+"-degree-dist-dict.pickle", "rb"))
	for el in sorted(dd):
		print el, "\t", dd[el]


def retweetsDist():
	rtCounter = pickle.load(open( "./out/"+TAG+"-rtcount-dist-dict.pickle", "rb"))
	for el in sorted(rtCounter):
		print el, "\t", rtCounter[el]


def computeCentrality():

	cty = pickle.load(open( "./out/"+TAG+"-cty-dict.pickle", "rb"))
	
	print "==== degree ==="
	for v in cty['degree'].values():
		print v
	print "==== betweeness ==="
	for v in cty['betweenness'].values():
		print v
	print "==== closeness ==="
	for v in 	cty['closeness'].values():
		print v
	print "==== eigenvector ==="
	for v in cty['eigenvector'].values():
			print v



def basicMarks(g):
	print "No node, no edges"
	print g.number_of_nodes(), g.number_of_edges()

def topNodes():
	cty = pickle.load(open( "./out/"+TAG+"-cty-dict.pickle", "rb"))


	print "==== degree ==="
        print sorted(cty['degree'], key=cty['degree'].get)[:55]
	print "==== betweeness ==="
        print sorted(cty['betweenness'], key=cty['betweenness'].get)[:55]
	print "==== closeness ==="
        print sorted(cty['closeness'], key=cty['closeness'].get)[:55]
	print "==== eigenvector ==="
        print sorted(cty['eigenvector'], key=cty['eigenvector'].get)[:55]
 

if __name__ == "__main__":
	G = readGPickle()
#	basicMarks(G)
#	draw(G)
#	degreeDist()
#	retweetsDist()
#	computeCentrality()
        topNodes()
