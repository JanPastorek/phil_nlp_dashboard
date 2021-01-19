import tweepy as tw
import re 
import json


def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys('api_keys.json')
consumer_key = keys['tw_consumer_key']
consumer_secret = keys['tw_consumer_secret']
access_token = keys['tw_access_token']
access_secret = keys['tw_access_secret']
bearer_token = keys['bearer_token']

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth)

def get_tweet_text(api, username):
    tweets = api.user_timeline(screen_name=username, 
                           count=100,
                           include_rts = False,
                           tweet_mode = 'extended')
    text_list = []
    for tweet in tweets:
        text_list.append(tweet.full_text)

    text = ' '.join(text_list)
    text = re.sub('&amp;', 'and', text)
    text = re.sub('_', ' ', text)
    remove_list = ["(?i)you'll", '(?i)you', '\sI\s', "I'm", "I'll", "I've", '(?i)\swe\s', "(?i)you're", "(?i)\syour\s", "(?i)they'll"
                   "(?i)they\s", "(?i)\stheir", "(?i)there's", "(?i)that's", '@', '(?i)\shtt[^\s]+', '(?i)\swww[^\s]+', '\s[^aI]\s',
                   "(?i)\sthey're"] 
    for item in remove_list:
        text = re.sub(r''+item+'', ' ', text)   
    return text

