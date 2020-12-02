import tweepy
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('stopwords')

consumer_key = "bbBt9FB9XcODqo9zoDQXYmIl0"
consumer_secret = "qgZy4KLEblYPDwvUP08CcGQ23vJig19lbOJHg31Z1DzYPPdArM"
access_token = "1329013165443739648-Tj3hRpOJiiR4MpuMPR9R7rpastliqz"
access_token_secret = "lxCtAJNeoaiIe9oWC7MyBuJ6jRyjgS1seCJilFE4Vtjgt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
all_tweets = tweepy.Cursor(api.search, q='Trump', lang = "en").items(100
                                                                     )
for tweet in all_tweets:
    tweets.append(tweet.text)
    

stop_words= set(stopwords.words("english"))
print(stop_words)

def Tokenizer(zin):
    nieuwe_zin = re.findall("\w{2,50}", str(zin))
    ignore = ['to','is','in','the','rt','and','of','on','it','co','https']
    cleaned_zin = [w.lower() for w in nieuwe_zin if w not in ignore]
    nieuw = Counter(cleaned_zin)
    return nieuw
    
print(Tokenizer(tweets))

vectorizer = CountVectorizer()
vectorizer.fit(tweets)
print(vectorizer.vocabulary_)
print(vector.shape)
print(vector.toarray())

for_df = []

for t in all_tweets:
    for_df.append({
            "user": t.user.screen_name, 
            "text": t.text,
            "created_at": t.created_at,
            "retweets": t.retweet_count
        })
    
df = pd.DataFrame.from_records(for_df)
df.head()ctorizer.transform(tweets)


