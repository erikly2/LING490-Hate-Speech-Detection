import tweepy
 
# API keyws that yous saved earlier
api_key = "1dWU3QayflekgFSnmnTur7841"
api_secrets = "Uqpty3X7zCQYgJ1ariHOkd2FS8xOaUadQ1S4TNGvJE8Rvd6gsA"
access_token = "1596710325063241730-Yo9eH11mWUz88aVZzeiIdOwFHfC67e"
access_secret = "OKxmWHX4kRb7YNhp9EUU3RcaRNKNqCX291QqO1wBSQClo"
 
# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key,api_secrets,access_token,access_secret)
#auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')