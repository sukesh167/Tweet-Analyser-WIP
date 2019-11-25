import flask
from flask import jsonify,request
import json
from processor import content

app = flask.Flask(__name__)
#render homepage
@app.route('/', methods=['GET'])
def home():
	wa=content()
	data = wa.trends
	return flask.render_template('home.html',trends=[[i['name'],
					('tweets - '+str(i['tweet_volume']))] for i in data])
#send data for viewing tweets
@app.route('/view', methods=['POST'])
def view():
	response = request.data
	response = json.loads(response)
	print(response['q'])
	wa=content()
	wa.tweet_search(response['q'])
	print(wa.tweets)
	return jsonify([[i.user_name,i.full_text,i.created_at,i.retweet_count] for i in wa.tweets])
#send words for wordcloud
@app.route('/wordcloud', methods=['POST'])
def wordcloud():
	response = request.data
	response = json.loads(response)
	print(response['q'])
	wa=content()
	wa.tweet_search(response['q'])
	wa.tweet_clean()
	print([k for j in [i.words for i in wa.clean_tweets] for k in j])
	return jsonify([k for j in [i.words for i in wa.clean_tweets] for k in j])
#do sentiment analysis and send sentiment values for set of tweets
@app.route('/charts', methods=['POST'])
def charts():
	response = request.data
	response = json.loads(response)
	print(response['q'])
	wa=content()
	wa.tweet_search(response['q'])
	wa.tweet_clean()
	wa.sentiment_analysis()
	negatives=[]
	positives=[]
	very_negative=[]
	very_positive=[]
	neutral=[]
	sentiments=[]
	#seperate tweets by sentiment
	for i in wa.clean_tweets:
		sentiments.append(i.sentiment)
		if i.sentiment=='Negative':
			negatives.extend([w for w in i.words])
		elif i.sentiment=='Positive':
			positives.extend([w for w in i.words])
		elif i.sentiment=='Verypositive':
			very_positive.extend([w for w in i.words])
		elif i.sentiment=='Verynegative':
			very_negative.extend([w for w in i.words])
		elif i.sentiment=='Neutral':
			neutral.extend([w for w in i.words])
		else:
			pass
	out=[]
	out.append(sentiments)
	out.append(negatives)
	out.append(positives)
	out.append(very_negative)
	out.append(very_positive)
	out.append(neutral)#tweets in different buckets for each sentiment type for future works 
	print(out)
	return jsonify(out)

if __name__=='__main__':
	app.run()#(debug=True) for debugging 
	

