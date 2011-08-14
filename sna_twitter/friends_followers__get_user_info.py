# -*- coding: utf-8 -*-

import sys
import json
import redis
from twitter__login import login
import functools

# A makeTwitterRequest call through to the /users/lookup 
# resource, which accepts a comma separated list of up 
# to 100 screen names. Details are fairly uninteresting. 
# See also http://dev.twitter.com/doc/get/users/lookup
from twitter__util import getUserInfo, _getFriendsOrFollowersUsingFunc




if __name__ == "__main__":
    screen_names = sys.argv[1:]

    t = login()
    r = redis.Redis()

    getFriends = functools.partial(_getFriendsOrFollowersUsingFunc, 
                               t.friends.ids, 'friend_ids', t, r)
    getFollowers = functools.partial(_getFriendsOrFollowersUsingFunc,
                                 t.followers.ids, 'follower_ids', t, r)

    getFriends(screen_names[0])
    getFollowers(screen_names[0])

    info = getUserInfo(t, r, screen_names=screen_names)
    r.sadd('oslo-ids',info[0]['id'])
    print "Appended oslo-ids. Now it has " + unicode(r.scard('oslo-ids'))    


#    print json.dumps(
#            info,
#            indent=4
#          )
