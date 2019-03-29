import tweepy
from textblob import TextBlob
import csv
import re
import sys
import pandas as pd

consumer_='QIbmvfekh74mPDUtQxTDYqoee'
consumer_secret='IgohTvOyFzkfxry0AruhQt3hb3eJGkXtYv1t7w58zwDFUfbXlj'
access_token_key='1056784423201398784-UkFf4MPrTDTP87r44mCDC6tbjJgWr6'
access_token_secret='idubMqUHVWqbsPDHJ6sOxMqxq80ggqdLEEFixGMUJWJB8'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
apin=tweepy.API(auth)
topicname='Football'
pubic_tweets=apin.search(topicname)
unwanted_words=['@','RT',':','https','http']
symbols=['@','#']
data=[]
for tweet in pubic_tweets:
    text=tweet.text
    textWords=text.split()
    #print (textWords)
    cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
    print (cleanedTweet)
    #print (TextBlob(cleanedTweet).tags)
    analysis= TextBlob(cleanedTweet)
    print (analysis.sentiment)
    polarity = 'Positive'
    if(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    if(0<=analysis.sentiment.polarity <=0.2):
        polarity = 'Neutral'
    print (polarity)
    dic={}
    dic['Sentiment']=polarity
    dic['Tweet']=cleanedTweet
    data.append(dic)
df=pd.DataFrame(data)
df.to_csv('analysis1.csv')
