from flask import Flask, render_template,redirect, url_for,flash
import pandas as pd
import datetime as dt

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET']) 
def index():
	return render_template('index.html')

@app.route('/result/<a>/<b>', methods=['POST', 'GET']) 
def result(a,b):
	data = pd.read_csv("/home/ckim48/mysite/static/preprocessed.csv")
	data['date'] = pd.to_datetime(data['date'])

	if a == "happy":
		data = data[data["mood"] == "happy"]
		if b == "sixty":
			data = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
		elif b == "zeros":
			data = data[data['date'].dt.year >1999 & (data['date'].dt.year < 2010)]
		elif b == "tenth":
			data = data[data['date'].dt.year >2009 & (data['date'].dt.year < 2020)]
		else:
			data = data[data['date'].dt.year >2019 & (data['date'].dt.year < 2030)]

	elif a== "sad":
		data = data[data["mood"] == "sad"]
		if b == "sixty":
			data = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
		elif b == "zeros":
			data = data[data['date'].dt.year >1999 & (data['date'].dt.year < 2010)]
		elif b == "tenth":
			data = data[data['date'].dt.year >2009 & (data['date'].dt.year < 2020)]
		else:
			data = data[data['date'].dt.year >2019 & (data['date'].dt.year < 2030)]

	elif a =="energetic":
		if b == "sixty":
			data = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
		elif b == "zeros":
			data = data[data['date'].dt.year >1999 & (data['date'].dt.year < 2010)]
		elif b == "tenth":
			data = data[data['date'].dt.year >2009 & (data['date'].dt.year < 2020)]
		else:
			data = data[data['date'].dt.year >2019 & (data['date'].dt.year < 2030)]
		data = data[data["mood"] == "energetic"]
	else:
		if b == "sixty":
			data = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
		elif b == "zeros":
			data = data[data['date'].dt.year >1999 & (data['date'].dt.year < 2010)]
		elif b == "tenth":
			data = data[data['date'].dt.year >2009 & (data['date'].dt.year < 2020)]
		else:
			data = data[data['date'].dt.year >2019 & (data['date'].dt.year < 2030)]
		data = data[data["mood"] == "calm"]
	c = data.sample(n = 8)
	dic = c.to_dict()

	artist_list = list(dic["artist"].values())
	music_list = list(dic["title"].values())
	sentiment_list = list(dic["sentiment"].values())
	sentiment_list2 = []
	for i in sentiment_list:
		sentiment_list2.append(100-i)
	return render_template('result.html',mood=a,years=b,dic=dic,artist_list=artist_list,music_list=music_list,sentiment_list=sentiment_list,sentiment_list2=sentiment_list2)

if __name__=="__main__":
  app.run(debug=True)