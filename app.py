from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import tweepy
import pyrebase
import time

app = Flask(__name__)

# Twitter API credentials
consumer_key = "c72Ktc4TlTxlcXraNP8VWuhwZ"
consumer_secret = "BuIqx2v5kIJitEeVnxd1gxMWoU5no3TDyEXNfxaDmuVFJyUczO"
access_token = "937993754350256129-4dJ0Hl3OYJqDSzPjOT9G6LLyCKcbhAU"
access_token_secret = "PB9x7N9vwxl9PPHIle1NkcfaLlbQM2QLddexV6W9CfeCE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
default_user = api.get_user('Google')

config = {
    "apiKey": "AIzaSyCFUqwqAS_l7MU631EZ9kWUv5dWqfe11us",
    "authDomain": "t-estproject.firebaseapp.com",
    "databaseURL": "https://t-estproject.firebaseio.com",
    "projectId": "t-estproject",
    "storageBucket": "t-estproject.appspot.com",
    "messagingSenderId": "636835135371"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/")
def chart():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values,
                           labels=labels,
                           chart_title='Follower Analytics',
                           follower_count=db.child('katyperry').child('followers_count').get().val(),
                           status_count=db.child('katyperry').child('statuses_count').get().val(),
                           tweets_count=12456,
                           following_count=db.child('katyperry').child('friends_count').get().val())



@app.route("/<username>/tweets")
def get_tweets(username):
    # Add the Code here
    return 'Hello'


@app.route("/<username>/follower")
def get_follower(username):
    total_followers = [0, ]
    labels = [i for i in range(0, 10)]
    user = api.get_user(username)
    count = 0
    while count <= len(labels):
        print('In loop')
        count += 1
        total_followers.append(user.followers_count / 1000000)
        time.sleep(1)

    return render_template('chart.html', values=total_followers, labels=labels,
                           follower_count=user.followers_count,
                           status_count=user.statuses_count,
                           tweets_count=12456,
                           following_count=user.friends_count)


if __name__ == "__main__":
    app.run()
