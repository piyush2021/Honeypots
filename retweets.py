

import tweepy
import time

consumer_key = "SDbxZcpf4hhIXJlyIAHHYu9EC"
consumer_secret = "aM6p0kUib8vDi8HATWt8cXXHius5H6S4VZqMYOAl9VgdUPG6nL"

access_token = "696664768795537408-1vY5HARSQDU1iFXTNmhxch7vECBL13Q"
access_token_secret = "lBFfY3ptJjS6WUL6Taz9T9vHJirRS12TdP0LU6y2lfizm"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = api.user_timeline('katyperry')[0]
temp_user = "xyz"
retweeter_list = []

for i in range(15):
	print ("loop no "+ str(i+1) + " going on.....")
	results = api.retweets(tweet.id,count = 80)
	for u in results:
		print (u.user.screen_name)
		if (temp_user==u.user.screen_name):
			break
		else:
			retweeter_list.append(u.user.screen_name)
	temp_user = results[0].user.screen_name
	time.sleep(60)

print ("\n".join(retweeter_list))

