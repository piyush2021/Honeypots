#Connecting to firebase database named as t-estproject (currently as public)
import pyrebase
#import json

config = {
    "apiKey": "AIzaSyCFUqwqAS_l7MU631EZ9kWUv5dWqfe11us",
    "authDomain": "t-estproject.firebaseapp.com",
    "databaseURL": "https://t-estproject.firebaseio.com",
    "projectId": "t-estproject",
    "storageBucket": "t-estproject.appspot.com",
    "messagingSenderId": "636835135371"
}

firebase = pyrebase.initialize_app(config)

fb = firebase.database()


import tweepy
import time
from datetime import datetime



def insert_user(username):

    temp_follower_id = 'yoyoyyoyo'
    temp_user = "xyz"
    count = 0
    while(1):


        

        consumer_key = ["SDbxZcpf4hhIXJlyIAHHYu9EC","c72Ktc4TlTxlcXraNP8VWuhwZ"]
        consumer_secret = ["aM6p0kUib8vDi8HATWt8cXXHius5H6S4VZqMYOAl9VgdUPG6nL","BuIqx2v5kIJitEeVnxd1gxMWoU5no3TDyEXNfxaDmuVFJyUczO"]
        access_token = ["696664768795537408-1vY5HARSQDU1iFXTNmhxch7vECBL13Q","937993754350256129-4dJ0Hl3OYJqDSzPjOT9G6LLyCKcbhAU"]
        access_token_secret = ["lBFfY3ptJjS6WUL6Taz9T9vHJirRS12TdP0LU6y2lfizm","PB9x7N9vwxl9PPHIle1NkcfaLlbQM2QLddexV6W9CfeCE"]
        auth = tweepy.OAuthHandler(consumer_key[count%2], consumer_secret[count%2])
        auth.set_access_token(access_token[count%2], access_token_secret[count%2])
        api = tweepy.API(auth)
        timeline = api.user_timeline(username)
        tweet = api.get_status(943572830179995648)
        
        count+=1
        start = time.time()
        print('I am in Loop '+str(count))

        user = api.get_user(username)
        DATA = {}

        DATA['created_at'] = str(user.created_at)
        DATA['description']=user.description
        DATA['entities']=user.entities
        DATA['favourites_count']=user.favourites_count
        DATA['followers_count']=user.followers_count
        DATA['friends_count']=user.friends_count
        DATA['geo_enabled']=user.geo_enabled
        DATA['ID']=user.id
        DATA['lang']=user.lang
        DATA['listed_count']=user.listed_count
        DATA['location']=user.location
        DATA['name']=user.name
        DATA['profile_use_background_image']=user.profile_use_background_image
        # _api stored as string (it's actually a json object)
        DATA['_api']=str(user._api)
        DATA['verified']=user.verified
        DATA['profile_sidebar_fill_color']=user.profile_sidebar_fill_color
        DATA['profile_text_color']=user.profile_text_color
        DATA['protected']=user.protected
        DATA['profile_background_color']=user.profile_background_color
        DATA['utc_offset']=user.utc_offset
        DATA['statuses_count']=user.statuses_count
        DATA['profile_link_color']=user.profile_link_color
        DATA['profile_image_url']=user.profile_image_url
        DATA['profile_background_image_url']=user.profile_background_image_url
        DATA['profile_background_tile']=user.profile_background_tile
        DATA['url']=user.url
        DATA['time_zone']=user.time_zone
        DATA['profile_sidebar_border_color']=user.profile_sidebar_border_color
        
        #print (time.time()-start)
        #print (time.time()-start)

        #count can be increased upto 5000 as per demand
        follower_list_class = api.followers(username,count = 100)
        new_follower_list = []
        

        
        followers_data = {}

        #adding new followers in a list

        for xyz in follower_list_class:

            personal_data = {}
            if (xyz.screen_name!=temp_follower_id):

                #created_at is saved in str due to datetime formaat
                personal_data['created_at']=str(xyz.created_at)
                personal_data['description']=xyz.description
                personal_data['entities']=xyz.entities
                personal_data['favourites_count']=xyz.favourites_count
                personal_data['followers_count']=xyz.followers_count
                personal_data['friends_count']=xyz.friends_count
                personal_data['geo_enabled']=xyz.geo_enabled
                personal_data['ID']=xyz.id
                personal_data['lang']=xyz.lang
                personal_data['listed_count']=xyz.listed_count
                personal_data['location']=xyz.location
                personal_data['name']=xyz.name
                personal_data['profile_use_background_image']=xyz.profile_use_background_image
                # _api stored as string (it's actually a json object)
                personal_data['_api']=str(xyz._api)
                personal_data['verified']=xyz.verified
                personal_data['profile_sidebar_fill_color']=xyz.profile_sidebar_fill_color
                personal_data['profile_text_color']=xyz.profile_text_color
                personal_data['protected']=xyz.protected
                personal_data['profile_background_color']=xyz.profile_background_color
                personal_data['utc_offset']=xyz.utc_offset
                personal_data['statuses_count']=xyz.statuses_count
                personal_data['profile_link_color']=xyz.profile_link_color
                personal_data['profile_image_url']=xyz.profile_image_url
                personal_data['profile_background_image_url']=xyz.profile_background_image_url
                personal_data['profile_background_tile']=xyz.profile_background_tile
                personal_data['url']=xyz.url
                personal_data['time_zone']=xyz.time_zone
                personal_data['profile_sidebar_border_color']=xyz.profile_sidebar_border_color
                #print (time.time()-start)
                #print (time.time()-start)
                new_follower_list.append(xyz.screen_name)

            else:
                break

            followers_data[xyz.screen_name] = personal_data

        #DATA['followers'] = followers_data
        
        temp_follower_id = follower_list_class[0].screen_name
        time_list = {}
        now = datetime.now()
        if new_follower_list is not []:
            time_list[str(now.year) + '-' + str(now.month) + '-' + str(now.day)+ ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)]=(' '.join(new_follower_list))
        #DATA['time_wise_followers'] = time_list
        #print (DATA)
        
        fb.child(user.screen_name).update(DATA)
        fb.child(user.screen_name).child('followers').update(followers_data)
        fb.child(user.screen_name).child('time_wise_followers').update(time_list)

        time_list_followers = {}
        if new_follower_list is not []:
            time_list_followers[str(now.year) + '-' + str(now.month) + '-' + str(now.day)+ ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)]=(' '.join(new_follower_list))
        #DATA['time_wise_followers'] = time_list_followers
        #print (DATA)

        
        retweeter_list = []
        retweeter_details_dict = {}
        
        results = api.retweets(943572830179995648,count = 80)
        for u in results:
            retweeter_personal_data = {}
            if (temp_user!=u.user.screen_name):
                #created_at is saved in str due to datetime formaat
                #print temp_user, u.user.screen_name
                retweeter_personal_data['created_at']=str(u.user.created_at)
                retweeter_personal_data['description']=u.user.description
                retweeter_personal_data['entities']=u.user.entities
                retweeter_personal_data['favourites_count']=u.user.favourites_count
                retweeter_personal_data['followers_count']=u.user.followers_count
                retweeter_personal_data['friends_count']=u.user.friends_count
                retweeter_personal_data['geo_enabled']=u.user.geo_enabled
                retweeter_personal_data['ID']=u.user.id
                retweeter_personal_data['lang']=u.user.lang
                retweeter_personal_data['listed_count']=u.user.listed_count
                retweeter_personal_data['location']=u.user.location
                retweeter_personal_data['name']=u.user.name
                retweeter_personal_data['profile_use_background_image']=u.user.profile_use_background_image
                # _api stored as string (it's actually a json object)
                retweeter_personal_data['_api']=str(u.user._api)
                retweeter_personal_data['verified']=u.user.verified
                retweeter_personal_data['profile_sidebar_fill_color']=u.user.profile_sidebar_fill_color
                retweeter_personal_data['profile_text_color']=u.user.profile_text_color
                retweeter_personal_data['protected']=u.user.protected
                retweeter_personal_data['profile_background_color']=u.user.profile_background_color
                retweeter_personal_data['utc_offset']=u.user.utc_offset
                retweeter_personal_data['statuses_count']=u.user.statuses_count
                retweeter_personal_data['profile_link_color']=u.user.profile_link_color
                retweeter_personal_data['profile_image_url']=u.user.profile_image_url
                retweeter_personal_data['profile_background_image_url']=u.user.profile_background_image_url
                retweeter_personal_data['profile_background_tile']=u.user.profile_background_tile
                retweeter_personal_data['url']=u.user.url
                retweeter_personal_data['time_zone']=u.user.time_zone
                retweeter_personal_data['profile_sidebar_border_color']=u.user.profile_sidebar_border_color

                retweeter_details_dict[u.user.screen_name] = retweeter_personal_data
                retweeter_list.append(u.user.screen_name)

            else:
                break
        



        temp_user = results[0].user.screen_name

        time_list_retweeters = {}
        if retweeter_list is not []:
            time_list_retweeters[str(now.year) + '-' + str(now.month) + '-' + str(now.day)+ ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)]=(' '.join(retweeter_list))



        follower_count_time_wise = {}
        follower_count_time_wise[str(now.year) + '-' + str(now.month) + '-' + str(now.day)+ ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)] = user.followers_count
        retweeter_count_time_wise = {}
        retweeter_count_time_wise[str(now.year) + '-' + str(now.month) + '-' + str(now.day)+ ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)] = tweet.retweet_count







        fb.child(user.screen_name).update(DATA)
        fb.child(user.screen_name).child('followers').update(followers_data)
        if len(new_follower_list)!= 0 :
            fb.child(user.screen_name).child('time_wise_followers').update(time_list_followers)
            fb.child(user.screen_name).child('time_wise_followers_count').update(follower_count_time_wise)
        fb.child(user.screen_name).child('retweeters').update(retweeter_details_dict)
        if len(retweeter_list) != 0 :
            fb.child(user.screen_name).child('time_wise_retweeters').update(time_list_retweeters)
            fb.child(user.screen_name).child('time_wise_retweeter_count').update(retweeter_count_time_wise)
        

        
        var = 60-(time.time()-start)
        var = max(0,var)
        print ("sleeping for "+str(var)+" seconds.......")
        time.sleep(var)



#variable username can be changed according to needs
username = 'katyperry'
#call function insert_user to insert user's details on database
insert_user(username)
