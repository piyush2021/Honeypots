#Connecting to firebase database named as t-estproject (currently as public)

from firebase import firebase

fb = firebase.FirebaseApplication('https://t-estproject.firebaseio.com/')


#setting up twitter api
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

        print('I am in Loop '+str(count))

        user = api.get_user(username)
        fb.put('/'+username,'created_at',user.created_at)
        fb.put('/'+username,'description',user.description)
        fb.put('/'+username,'entities',user.entities)
        fb.put('/'+username,'favourites_count',user.favourites_count)
        fb.put('/'+username,'followers_count',user.followers_count)
        fb.put('/'+username,'friends_count',user.friends_count)
        fb.put('/'+username,'geo_enabled',user.geo_enabled)
        fb.put('/'+username,'ID',user.id)
        fb.put('/'+username,'lang',user.lang)
        fb.put('/'+username,'listed_count',user.listed_count)
        fb.put('/'+username,'location',user.location)
        fb.put('/'+username,'name',user.name)
        fb.put('/'+username,'profile_use_background_image',user.profile_use_background_image)
        # _api stored as string (it's actually a json object)
        fb.put('/'+username,'_api',str(user._api))
        fb.put('/'+username,'verified',user.verified)
        fb.put('/'+username,'profile_sidebar_fill_color',user.profile_sidebar_fill_color)
        fb.put('/'+username,'profile_text_color',user.profile_text_color)
        fb.put('/'+username,'protected',user.protected)
        fb.put('/'+username,'profile_background_color',user.profile_background_color)
        fb.put('/'+username,'utc_offset',user.utc_offset)
        fb.put('/'+username,'statuses_count',user.statuses_count)
        fb.put('/'+username,'profile_link_color',user.profile_link_color)
        fb.put('/'+username,'profile_image_url',user.profile_image_url)
        fb.put('/'+username,'profile_background_image_url',user.profile_background_image_url)
        fb.put('/'+username,'profile_background_tile',user.profile_background_tile)
        fb.put('/'+username,'url',user.url)
        fb.put('/'+username,'time_zone',user.time_zone)
        fb.put('/'+username,'profile_sidebar_border_color',user.profile_sidebar_border_color)


        #count can be increased upto 5000 as per demand
        follower_list_class = api.followers(username,count = 100)
        new_follower_list = []

        #adding new followers in a list

        for xyz in follower_list_class:
            if (xyz.screen_name!=temp_follower_id):


                fb.put('/'+username+'/followers/'+xyz.screen_name,'created_at',xyz.created_at)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'description',xyz.description)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'entities',xyz.entities)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'favourites_count',xyz.favourites_count)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'followers_count',xyz.followers_count)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'friends_count',xyz.friends_count)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'geo_enabled',xyz.geo_enabled)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'ID',xyz.id)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'lang',xyz.lang)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'listed_count',xyz.listed_count)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'location',xyz.location)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'name',xyz.name)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_use_background_image',xyz.profile_use_background_image)
                # _api stored as string (it's actually a json object)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'_api',str(xyz._api))
                fb.put('/'+username+'/followers/'+xyz.screen_name,'verified',xyz.verified)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_sidebar_fill_color',xyz.profile_sidebar_fill_color)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_text_color',xyz.profile_text_color)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'protected',xyz.protected)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_background_color',xyz.profile_background_color)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'utc_offset',xyz.utc_offset)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'statuses_count',xyz.statuses_count)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_link_color',xyz.profile_link_color)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_image_url',xyz.profile_image_url)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_background_image_url',xyz.profile_background_image_url)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_background_tile',xyz.profile_background_tile)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'url',xyz.url)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'time_zone',xyz.time_zone)
                fb.put('/'+username+'/followers/'+xyz.screen_name,'profile_sidebar_border_color',xyz.profile_sidebar_border_color)

                new_follower_list.append(xyz.screen_name)

            else:
                break

        temp_follower_id = follower_list_class[0].screen_name

        if new_follower_list is not []:
            fb.put('/'+username+'/time_database_followers',time.ctime(),(' '.join(new_follower_list)))

        time.sleep(60)



#variable username can be changed according to needs
username = 'katyperry'
#call function insert_user to insert user's details on database
insert_user(username)


