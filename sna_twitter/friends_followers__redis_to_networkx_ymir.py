# -*- coding: utf-8 -*-

# Summary: Build up a digraph where an edge exists between two users 
# if the source node is following the destination node

import os
import sys
import json
import networkx as nx
import redis
#import matplotlib.pyplot as plt

from twitter__util import getRedisIdByScreenName
from twitter__util import getRedisIdByUserId


g = nx.Graph()
r = redis.Redis()


LIST_NAME = "oslo-ids"

starting_ids = list(r.smembers(LIST_NAME))
print starting_ids




# Compute all ids for nodes appearing in the graph
for _id in starting_ids:
	friend_ids = list(r.smembers(getRedisIdByUserId(_id, 'friend_ids')))
	id_for_screen_name = _id
	ids = [id_for_screen_name] + friend_ids

	for current_id in ids:
		print >> sys.stderr, 'Processing user with id', current_id

		try:
			raw_current_info = r.get(getRedisIdByUserId(current_id, 'info.json'
									  ))
			if not raw_current_info:
				# try to get it one more time
				print "Making req to Twitter API"
				os.system('python friends_followers__get_user_info_by_id.py ' + current_id)

			current_info = json.loads(r.get(getRedisIdByUserId(current_id, 'info.json'
									  )))

			current_screen_name = current_info['screen_name']
			friend_ids = list(r.smembers(getRedisIdByScreenName(current_screen_name,
							  'friend_ids')))

			# filter out ids for this person if they aren't also SCREEN_NAME's friends too, 
			# which is the basis of the query

			friend_ids = [fid for fid in friend_ids if fid in starting_ids] # TODO czy to nie dziala?
		except Exception, e:
			print >> sys.stderr, 'Problems with', current_id


		for friend_id in friend_ids:
			if friend_id in starting_ids:
				try:
					raw_friend_info = r.get(getRedisIdByUserId(friend_id, 'info.json'))

					if not raw_friend_info:
						# try to get it one more time
						print "Making req to Twitter API"
						os.system('python friends_followers__get_user_info_by_id.py ' + friend_id)
					
					friend_info = json.loads(r.get(getRedisIdByUserId(friend_id,
											 'info.json')))

				except TypeError, e:
					print >> sys.stderr, '\tSkipping', friend_id, 'for', current_screen_name
					continue

				g.add_edge(current_screen_name, friend_info['screen_name'])
				print 'Added edge from ', current_screen_name, ' to ', friend_info['screen_name']

# Pickle the graph to disk...

if not os.path.isdir('out'):
	os.mkdir('out')

## ymir
print g.nodes()
#nx.draw(g)
#plt.show()

filename = os.path.join('out', LIST_NAME + '.gpickle')
nx.write_gpickle(g, filename)

print 'Pickle file stored in: %s' % filename

# You can un-pickle like so...

# g = nx.read_gpickle(os.path.join('out', SCREEN_NAME + '.gpickle'))
