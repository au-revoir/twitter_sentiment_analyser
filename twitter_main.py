from tweepy import Stream
from tweepy import OAuthHandler

import json

import sentiment_mod as s

#Enter your api tokens
ckey="************"
csecret="***********"
atoken="*************"
asecret="************"

from twitterapistuff import *

class my_listener(tweepy.StreamListener):

    def on_data(self, data):

	    all_data = json.loads(data)

	    tweet = all_data["text"]
	    senti, conf = s.sentiment(tweet)
	    print(tweet, sentiment_value, confidence)

	    if conf*1000 >= 90:
		    output = open("output.txt","a")
		    output.write(senti)
		    output.write('\n')
		    output.close()

	    return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["gst"])

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("output.txt","r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
