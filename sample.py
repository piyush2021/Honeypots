import pyrebase

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

user = db.child("katyperry").child("time_wise_followers_count").order_by_key().limit_to_last(10).get().val()

print(list(user.values()))
print(list(user.keys()))