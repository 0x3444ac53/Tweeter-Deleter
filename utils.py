import tweepy

def get_instance(keys):
    auth = tweepy.OAuthHandler(keys['api_key'], keys['secret'])
    auth.set_access_token(keys['a_token'], keys['a_secret'])
    api = tweepy.API(auth)
    return api

def get_authorized(keys : dict):
    auth = tweepy.OAuthHandler(keys['api_key'], keys['secret'])
    try:
        print(f"go here: {auth.get_authorization_url()}")
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    verifier = input("GIVE ME: ")
    token = auth.get_access_token(verifier)
    try:
        with open('muhKEYS', 'w') as f:
            f.write(auth.access_token + '\n')
            f.write(auth.access_token_secret)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')
    return tweepy.API(auth)

