# Tweet-Streamer-Analyser

##Web app to show tweets, show WordCloud of tweets, Sentiment analysis of tweets for a given user or #tag

###The web app contains both streamer dashboard and analysis dashboad in the same page

###Done using [flask](https://www.palletsprojects.com/p/flask/) as backend,

###packages used :-
* [Tweepy](https://tweepy.readthedocs.io/en/latest/) to access twitter API
* [tweet-preprocessor](https://pypi.org/project/tweet-preprocessor/) for cleaning the tweets
* [pycorenlp](https://pypi.org/project/pycorenlp/) for sentiment analysis.

##To run the web app the server for stanfordcorenlp has to be started

1) Download and unzip StanfordCoreNLP(done in ubuntu):
 
 ```wget https://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip https://nlp.stanford.edu/software/stanford-english-corenlp-2018-10-05-models.jar```
 
```unzip stanford-corenlp-full-2018-10-05.zip```

2) Setup packages for english:

```mv stanford-english-corenlp-2018-10-05-models.jar stanford-corenlp-full-2018-10-05```

3) Start the server:

```cd stanford-corenlp-full-2018-10-05```

```java -mx6g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 5000```

(change timeout for more data transfer, change -mx6g for amount of memory used by server( 2g, 4g ... )

##Start the web app by running web_app.py 

###the streamer uses jinja input and script to display the tweets 
###whereas the analyser creates svg to display worcloud and pie chart

##Future works:
* Caching the searches and data for quicke display as Twitter API and StanfordCoreNLP take significant time
* Adding more Charts of sentiment analysis such as most used words in negative, positive sentiments
* Adding location in script so as to display the trending #tags locally for the user of webapp
* Adding search output filters such as time limit and number of tweets limit 
* Having Different pages for Stremer and Analyser
* Including more images and links in the webpage to better the user experience

