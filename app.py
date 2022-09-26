from flask import Flask, render_template,redirect, url_for,flash,request
import pandas as pd
import datetime as dt
import sys
import asyncio
import tkinter as tk
import sys
from io import StringIO
from collections import defaultdict
import string
import time
import json
from nlp_runner2 import nlp_runner
from textblob import TextBlob


app = Flask(__name__)
output = {}
A = []
chk={}
AA = []
@app.route('/', methods=['POST', 'GET']) 
def index():
	return render_template('index.html')
#/home/ckim48/mysite/
@app.route('/result/<a>/<b>', methods=['POST', 'GET']) 
def result(a,b):
	data = pd.read_csv("/home/ckim48/mysite/static/preprocessed.csv")
	data['date'] = pd.to_datetime(data['date'])

	if a == "happy":
		data = data[data["mood"] == "happy"]
		if b == "sixty":
			print("A",file=sys.stderr)
			# mask = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
			data = data[data['date'].between('1900', '1999')]
		elif b == "zeros":
			data = data[data['date'].between('2000', '2009')]
		elif b == "tenth":
			data = data[data['date'].between('2010', '2019')]
		else:
			data = data[data['date'].between('2020', '2030')]

		
	elif a== "sad":
		data = data[data["mood"] == "sad"]
		if b == "sixty":
			print("A",file=sys.stderr)
			# mask = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
			data = data[data['date'].between('1900', '1999')]
		elif b == "zeros":
			data = data[data['date'].between('2000', '2009')]
		elif b == "tenth":
			data = data[data['date'].between('2010', '2019')]
		else:
			data = data[data['date'].between('2020', '2030')]

	elif a =="energetic":
		data = data[data["mood"] == "energetic"]
		if b == "sixty":
			print("A",file=sys.stderr)
			# mask = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
			data = data[data['date'].between('1900', '1999')]
		elif b == "zeros":
			data = data[data['date'].between('2000', '2009')]
		elif b == "tenth":
			data = data[data['date'].between('2010', '2019')]
		else:
			data = data[data['date'].between('2020', '2030')]
		
	else:
		data = data[data["mood"] == "calm"]
		if b == "sixty":
			print("A",file=sys.stderr)
			# mask = data[data['date'].dt.year >1900 & (data['date'].dt.year < 2000)]
			data = data[data['date'].between('1900', '1999')]
		elif b == "zeros":
			data = data[data['date'].between('2000', '2009')]
		elif b == "tenth":
			data = data[data['date'].between('2010', '2019')]
		else:
			data = data[data['date'].between('2020', '2030')]
	if len(data) > 8:
		c = data.sample(n = 8)
	else:
		c = data.sample(len(data))
	dic = c.to_dict()

	artist_list = list(dic["artist"].values())
	music_list = list(dic["title"].values())
	sentiment_list = list(dic["sentiment"].values())
	sentiment_list2 = []
	for i in sentiment_list:
		sentiment_list2.append(100-i)
	return render_template('result.html',mood=a,years=b,dic=dic,artist_list=artist_list,music_list=music_list,sentiment_list=sentiment_list,sentiment_list2=sentiment_list2)

@app.route('/result2', methods=['POST', 'GET'])
def result2():
	res = []
	artist = request.form.get('artist')
	title = request.form.get('title')

	output = handle_reddit_crawler(artist,title)
	lst3 = []
	pos = 1
	neg = 1
	sum_por = 0
	if output == "None":
		content_lst = "None"
		len2 = 0
	else:
		with open('/home/ckim48/mysite/keydict_list.json') as json_file:
			data = json.load(json_file)
		content_lst = []
		len2 = 0
		for i in range(0,len(data)):
			if data[i]["title"] != "":
				content_lst.append(data[i]["title"])
		for i in content_lst:
			temp_t = TextBlob(i)
			lst3.append((temp_t.sentiment.polarity))
		for j in lst3:
			if j < 0:
				neg+=1
			else:
				pos+=1 #mock
		len2 = len(content_lst)
		avg_por =(pos+2)/((neg-2)+pos)
	print(content_lst)
	avg_por_rev = 100-avg_por
	# global A
	# A = list(output.keys())
	# for i in range(len(A)):
	# 	a = showComments(A[i])
	# 	res.append(a)

	# print("AAAAAAAAAAAAAAAA:",a,file=sys.stderr)
	return render_template('result2.html',artist=artist,title=title,output=output,len=len(output),content_lst=content_lst,len2=len2,avg_por=avg_por,avg_por_rev=avg_por_rev)


def handle_reddit_crawler(a,b):
    # IMPORTANT  main.py __main__ goes here
    print("handling reddit crawler.......processing...")
    global output

    output = nlp_runner(b, a).main()
    
    print("about to return..")

    return output

def showComments(key):
    i = 0
    chk[key] = 1
    global AA
    for m, j in enumerate(output[key][1]):
        sentence = output[key][1][m].split()

        psum = [0] * (len(sentence)+5)
        psum[0] = len(sentence[0]) + 17
        for k in range(1, len(sentence)):
            psum[k] += psum[k-1] + len(sentence[k]) + 17

        index_label = str(m+1)

        AA.append(index_label)

        for wordIndex in range(0, len(sentence)):
            handled_spacing = 0
            if wordIndex == 0:
                handled_spacing = 200
            else:
                handled_spacing = 200 + psum[wordIndex-1]*2.8

            if(wordIndex not in output[key][2][m]):
                text = sentence[wordIndex]
            else:
                if output[key][0] < 0.3:
                    text = sentence[wordIndex]
                else:
                    text = sentence[wordIndex]
        AA.append(text)
        return AA

        i += 1
if __name__=="__main__":
  app.run(debug=True)