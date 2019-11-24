import flask
from flask import jsonify,request
import json
from processor import content

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	wa=content()
	data = wa.trends
	return flask.render_template('home.html',trends=[[i['name'],
					('tweets - '+str(i['tweet_volume']))] for i in data])

@app.route('/view', methods=['POST'])
def view():
	response = request.data
	response = json.loads(response)
	print(response['q'])
	wa=content()
	wa.tweet_search(response['q'])
	print(wa.tweets)
	return jsonify([[i.user_name,i.full_text,i.created_at,i.retweet_count] for i in wa.tweets])

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
	neutral=[]
	sentiments=[]
	for i in wa.clean_tweets:
		sentiments.append(i.sentiment)
		if i.sentiment=='Negative':
			negatives.extend([w for w in i.words])
		elif i.sentiment=='Positive':
			positives.extend([w for w in i.words])
		else:
			neutral.extend([w for w in i.words])
	out=[]
	out.append(sentiments)
	out.append(negatives)
	out.append(positives)
	out.append(neutral)
	print(out)
	return jsonify(out)

if __name__=='__main__':
	app.run(debug=True)
	

