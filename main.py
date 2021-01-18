from utils import *
from keys import keys

def tweeter_deleter():
    api = get_authorized(keys)
    timeline = tweepy.Cursor(api.user_timeline).items()
    for tweet in timeline:
        print(tweet.id)
        api.destroy_status(tweet.id)

tweeter_deleter()
