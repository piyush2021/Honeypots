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
   friend_temp = 0
   temp_follower_id = 'abcd'


   while True:
       count += 1
       print('I am in Loop ' + str(count))
       # Getting the information about the user.
       user = api.get_user(username)
       friend = user.friends_count
       status = user.statuses_count
       follower = user.followers_count
       follower_list_class = api.followers(username,count = 100)
       new_follower_list = []

       #adding new followers in a list
       for xyz in follower_list_class:

        if (xyz.screen_name!=temp_follower_id):
          new_follower_list.append(xyz.screen_name)
        else:
          break

       temp_follower_id = follower_list_class[0].screen_name

       # Executing an SQL statement to send to the database.
       #cur.execute("INSERT INTO twitter_stats (username, follower_count, status_count) VALUES (?, ?, ?)", (username, '123', '456'))
       if (status_temp!=status or follower_temp!=follower or friend!=friend_temp):
           cur.execute("INSERT INTO twitter_stats (username, time, following_count,follower_count, status_count,new_followers) VALUES (?, ?, ?, ?, ?, ?)", (username, time.ctime(),friend, follower, status, " ".join(new_follower_list)))
           con.commit()
           follower_temp = follower
           status_temp = status
           friend_temp = friend

       time.sleep(60)

   con.close()

users = ['twitter', 'VENETHIS', 'katyperry', 'justinbieber', '6BillionPeople']
insert_user('katyperry')
