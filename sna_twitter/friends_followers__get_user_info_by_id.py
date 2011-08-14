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
    uid = sys.argv[1:]

    t = login()
    r = redis.Redis()

    info = getUserInfo(t, r, user_ids=uid)