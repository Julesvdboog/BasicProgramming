import tweepy
from textblob import TextBlob

consumer_key = "bbBt9FB9XcODqo9zoDQXYmIl0"
consumer_secret = "qgZy4KLEblYPDwvUP08CcGQ23vJig19lbOJHg31Z1DzYPPdArM"
access_token = "1329013165443739648-Tj3hRpOJiiR4MpuMPR9R7rpastliqz"
access_token_secret = "lxCtAJNeoaiIe9oWC7MyBuJ6jRyjgS1seCJilFE4Vtjgt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

public_tweets = api.search('Trump', count = 100000, lang = "en", until = "2020-11-20")
for tweet in public_tweets:
    tweets.append(tweet)


print(len(tweets))


