import sqlite3 as sql
import tweepy
import time

# Twitter API credentials
consumer_key = "c72Ktc4TlTxlcXraNP8VWuhwZ"
consumer_secret = "BuIqx2v5kIJitEeVnxd1gxMWoU5no3TDyEXNfxaDmuVFJyUczO"
access_token = "937993754350256129-4dJ0Hl3OYJqDSzPjOT9G6LLyCKcbhAU"
access_token_secret = "PB9x7N9vwxl9PPHIle1NkcfaLlbQM2QLddexV6W9CfeCE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def insert_user(username):
    # Creating the database
    con = sql.connect("database.db")
    cur = con.cursor()
    count = 0
    follower_temp = 0
    status_temp = 0
    while True:
        count += 1
        print('I am in Loop ' + str(count))
        # Getting the information about the user.
        user = api.get_user(username)
        follower = user.followers_count
        status = user.statuses_count
        # Executing an SQL statement to send to the database.
        #cur.execute("INSERT INTO twitter_stats (username, follower_count, status_count) VALUES (?, ?, ?)", (username, '123', '456'))
        if (status_temp!=status or follower_temp!=follower):
            cur.execute("INSERT INTO twitter_stats (username, time, follower_count, status_count) VALUES (?, ?, ?, ?)", (username, time.ctime(), follower, status))
            con.commit()
            follower_temp = follower
            status_temp = status

        time.sleep(60)

    con.close()
users = ['ShahrukhKhan', 'KatrinaKaif', 'SachinTendulkar', 'piyushbhatia993', 'SundarPichai']
insert_user('katyperry')