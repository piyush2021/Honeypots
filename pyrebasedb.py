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

consumer_key = "SDbxZcpf4hhIXJlyIAHHYu9EC"
consumer_secret = "aM6p0kUib8vDi8HATWt8cXXHius5H6S4VZqMYOAl9VgdUPG6nL"
access_token = "696664768795537408-1vY5HARSQDU1iFXTNmhxch7vECBL13Q"
access_token_secret = "lBFfY3ptJjS6WUL6Taz9T9vHJirRS12TdP0LU6y2lfizm"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def insert_user(username):

    temp_follower_id = 'yoyoyyoyo'
    count = 0
    
    for i in range(10):

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
        print (time.time()-start)

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
                print (time.time()-start)
                new_follower_list.append(xyz.screen_name)

            else:
                break

            followers_data[xyz.screen_name] = personal_data

        #DATA['followers'] = followers_data
        
        temp_follower_id = follower_list_class[0].screen_name
        time_list = {}
        if new_follower_list is not []:
            time_list[time.ctime()]=(' '.join(new_follower_list))
        #DATA['time_wise_followers'] = time_list
        #print (DATA)

        fb.child(user.screen_name).update(DATA)
        fb.child(user.screen_name).child('followers').update(followers_data)
        fb.child(user.screen_name).child('time_wise_followers').update(time_list)

        time.sleep(60-(time.time()-start))



#variable username can be changed according to needs
username = 'katyperry'
#call function insert_user to insert user's details on database
insert_user(username)


