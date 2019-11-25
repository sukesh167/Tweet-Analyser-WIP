# -*- coding: utf-8 -*-
#processing all data for webapp
from cleaner import cleaning
from tweepy import OAuthHandler, API, Cursor
from pycorenlp import StanfordCoreNLP
#class to create tweet object with username, full tweet, words in tweet, preprocessed tweet, and sentiments
  
class get_tweets():
	def __init__(self,tweet):
		self.tweets=tweet
		self.created_at=tweet.created_at
		self.user_name=tweet.user.name
		self.full_text=tweet.full_text
		self.words=None
		self.clean_text=None
		self.retweet_count=tweet.retweet_count.real
		self.verified_user=tweet.user.verified
		self.sentiment=None
		self.sentiment_value=None

class content():
	def __init__(self):
		self.clean_tweets=None
		self.tweets=[]
		#enter twitter API access details here
		ACCESS_TOKEN = 'access token'
		ACCESS_TOKEN_SECRET = 'access token secret'
		CONSUMER_KEY = 'consumer key'
		CONSUMER_SECRET = 'comsumer secret'
		
		auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = API(auth, wait_on_rate_limit=True)
		self.trends=self.api.trends_place(1)[0]['trends'][:5]	
        #Search tweets for given # or username
	def tweet_search(self,query):
		for tweet in Cursor(self.api.search, q=query, lang="en", 
							tweet_mode="extended").items():
			self.tweets.append(get_tweets(tweet))
	#Preprocess the tweets and get clean tweets and words in tweets	
	def tweet_clean(self):
		self.clean_tweets=cleaning(self.tweets).clean_tweets
        #Sentiment analysis using StanfordNLP 
	def sentiment_analysis(self):
		nlp = StanfordCoreNLP('http://localhost:9000')#enter local host port if changed
		for text in self.clean_tweets:
			result = nlp.annotate(text.clean_text,
					properties={
					'annotators': 'sentiment',
					'outputFormat': 'json',
					'timeout' : 75000})#change timeout for higher data transfer
			
			for s in result["sentences"]:
				text.sentiment=s["sentiment"]
				text.sentiment_value=s["sentimentValue"]
	


