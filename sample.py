import tweepy
# Twitter API credentials
consumer_key = "c72Ktc4TlTxlcXraNP8VWuhwZ"
consumer_secret = "BuIqx2v5kIJitEeVnxd1gxMWoU5no3TDyEXNfxaDmuVFJyUczO"
access_token = "937993754350256129-4dJ0Hl3OYJqDSzPjOT9G6LLyCKcbhAU"
access_token_secret = "PB9x7N9vwxl9PPHIle1NkcfaLlbQM2QLddexV6W9CfeCE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.get_status(943572830179995648)
tweets = tweets.text
print(tweets)

