import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Retorna tweets por pelo usuário
name = "kblock43"
tweetCount = 10
results = api.user_timeline(id=name, count=tweetCount, tweet_mode='extended')

for tweet in results:
    print("___________________________________________________________________________________________________________")
    print(tweet.created_at)
    print(tweet.full_text)
    print("___________________________________________________________________________________________________________")


#Retorna tweets pela hashtag determinada
query = "#kblock43"
results = api.search(q=query, count=20,  tweet_mode='extended')

for tweet in results:
    print("___________________________________________________________________________________________________________")
    print(tweet.created_at)
    print(tweet.user.screen_name,"Tweeted:",tweet.full_text)
    print("___________________________________________________________________________________________________________")
