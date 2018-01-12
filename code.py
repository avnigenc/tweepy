import tweepy

consumer_key = ‘yours consumer_key’
consumer_secret = ‘yours consumer_secret’
access_token = ‘yours access_token’
access_token_secret = yours access_token_secret’



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status(status=”this is a sample tweet using tweepy with python”)

user = api.get_user('avnigenc')

print("Name:", user.name)
print("User id: ", user.id_str)
print("Description: ", user.description)
print("Location:",user.location)
print("Time zone: ", user.time_zone)
print("Number of Following:",user.friends_count)
print("Number of Followers:",user.followers_count)
print("Number of tweets: ", str(user.statuses_count))
