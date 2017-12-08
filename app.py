from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import tweepy
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

@app.route("/")
def chart():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values,
                           labels=labels, chart_title='Follower Analytics',
                           follower_count=default_user.followers_count,
                           status_count=default_user.statuses_count,
                           tweets_count=12456,
                           following_count=default_user.friends_count)


@app.route("/<username>/tweets")
def get_tweets(username):
    # Add the Code here
    return 'Hello'


@app.route("/<username>/follower")
def get_follower(username):
    # Add the Code here
    start_time = time.time()
    total_followers = [0, ]
    time_elapsed = [0, ]
    user = api.get_user(username)
    count = 0
    while True:
        print('In loop')
        total_followers.append(user.followers_count)
        time_elapsed.append(time.time() - start_time)
        count += 1
        if count == 10:
            return render_template('chart.html', values=total_followers, labels=time_elapsed)


if __name__ == "__main__":
    app.run()
