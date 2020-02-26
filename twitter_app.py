import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


user = api.get_user("teetoye")

print(user.name)

print(user.description)

print(user.status.text)

followers=[]

cursor = tweepy.Cursor(api.followers, screen_name='teetoye')

for account in cursor.items(10):
    followers.append(account.screen_name)

print(followers)

#print('followers:',' ' .join(sorted(followers, keys=lamda s:s.lower)))


