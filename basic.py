from __future__ import unicode_literals
from pattern.en import sentiment as sentiment_en
import tweepy
from textblob import TextBlob
import re
from collections import Counter


consumer_key = "bbBt9FB9XcODqo9zoDQXYmIl0"
consumer_secret = "qgZy4KLEblYPDwvUP08CcGQ23vJig19lbOJHg31Z1DzYPPdArM"
access_token = "1329013165443739648-Tj3hRpOJiiR4MpuMPR9R7rpastliqz"
access_token_secret = "lxCtAJNeoaiIe9oWC7MyBuJ6jRyjgS1seCJilFE4Vtjgt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

all_tweets = tweepy.Cursor(api.search, q='Trump', lang = "en").items(100)

for tweet in all_tweets:
    tweets.append(tweet.text)
    
    
 
def Tokenizer(zin):
    nieuwe_zin = re.findall("\w+", str(zin))
    ignore = ['to','is','in']
    cleaned_zin = [w.lower() for w in nieuwe_zin if w not in ignore]
    nieuw = Counter(cleaned_zin)
    return nieuw
    

print(Tokenizer(tweets))

STOP_WORDS = set(tweets)

for tweet in all_tweets:
    tweets.count(tweet.text)

for tweet in all_tweets:
    polarity, subjectivity = sentiment_en(tweets)
    print(polarity, subjectivity)

