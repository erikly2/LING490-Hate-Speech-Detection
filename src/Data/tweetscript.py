import requests
import os
import json
from requests_oauthlib import OAuth1Session
import json

# # To set your enviornment variables in your terminal run the following line:
# # export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN0ejwEAAAAAG6RofdC3LcMq4iTMeUG%2F2MDWPa4%3DtEZKKeXijG7h4f9BUfdJrMrZy9zKIFAjlrqUldJkZ3VbOrNrYZ"
f = open("hatespeech.txt", "w")
consumer_key = "1dWU3QayflekgFSnmnTur7841"
consumer_secret = "Uqpty3X7zCQYgJ1ariHOkd2FS8xOaUadQ1S4TNGvJE8Rvd6gsA"
params = {"ids": "565900500273750019", "tweet.fields": "created_at"}


request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

    # Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)


access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]


id_list = []
def getIds():
    file = open("ids.txt", "r")
    for sentence in file:
        splitted = sentence.split(",")
        id = splitted[0]
        id_list.append(id)

def connect_to_endpoint(ids):
    response = oauth.get(
    "https://api.twitter.com/2/tweets", params = {"ids":ids}
    )
    print("response")
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json(), response.status_code


def main():

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    getIds()
    subslist = []
    x = 0
    while x < len(id_list):
        if(x+100>len(id_list)):
            subset = id_list[x:len(id_list)]
            subslist.append(subset)
            break;
        subset = id_list[x:x+100]
        subslist.append(subset)
        x = x+100
    
    ids = ",".join(id_list[0:99])
    # print(ids)
    #url = create_url(ids)
    json_response, rep = connect_to_endpoint(ids)
    # print(json_response)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    # for datapiece in json_response["data"]:
    #     f.write(datapiece["text"] + "\n")

    var = 0
    for subset in subslist:
        ids = ",".join(subset)
        #url = create_url(ids)
        json_response, rep = connect_to_endpoint(ids)
        # print(json_response)
        # print(json.dumps(json_response, indent=4, sort_keys=True))
        if("data" not in json_response):
            break
        for datapiece in json_response["data"]:
            print("here")
            print(var)
            var += 1
            f.write(datapiece["text"] + "\n")

if __name__ == "__main__":
    main()


# def create_url(ids):
#     tweet_fields = "tweet.fields=lang,author_id"
#     idparam = "ids=" + ids
#     #ids = "ids=1278747501642657792,1255542774432063488"
#     # You can adjust ids to include a single Tweets.
#     # Or you can add to up to 100 comma-separated IDs
#     url = "https://api.twitter.com/2/tweets?{}&{}".format(idparam, tweet_fields)
#     return url


# def bearer_oauth(r):
#     """
#     Method required by bearer token authentication.
#     """

#     r.headers["Authorization"] = f"Bearer {bearer_token}"
#     r.headers["User-Agent"] = "v2TweetLookupPython"
#     return r



# # To set your enviornment variables in your terminal run the following line:
# # export 'CONSUMER_KEY'='<your_consumer_key>'
# # export 'CONSUMER_SECRET'='<your_consumer_secret>'

# consumer_key = "1dWU3QayflekgFSnmnTur7841"
# consumer_secret = "Uqpty3X7zCQYgJ1ariHOkd2FS8xOaUadQ1S4TNGvJE8Rvd6gsA"

# # You can adjust ids to include a single Tweets
# # Or you can add to up to 100 comma-separated IDs
# params = {"ids": "565900500273750019", "tweet.fields": "created_at"}

# request_token_url = "https://api.twitter.com/oauth/request_token"
# oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

# try:
#     fetch_response = oauth.fetch_request_token(request_token_url)
# except ValueError:
#     print(
#         "There may have been an issue with the consumer_key or consumer_secret you entered."
#     )

# resource_owner_key = fetch_response.get("oauth_token")
# resource_owner_secret = fetch_response.get("oauth_token_secret")
# print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
# base_authorization_url = "https://api.twitter.com/oauth/authorize"
# authorization_url = oauth.authorization_url(base_authorization_url)
# print("Please go here and authorize: %s" % authorization_url)
# verifier = input("Paste the PIN here: ")

# # Get the access token
# access_token_url = "https://api.twitter.com/oauth/access_token"
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=resource_owner_key,
#     resource_owner_secret=resource_owner_secret,
#     verifier=verifier,
# )
# oauth_tokens = oauth.fetch_access_token(access_token_url)


# access_token = oauth_tokens["oauth_token"]
# access_token_secret = oauth_tokens["oauth_token_secret"]

# # Make the request
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=access_token,
#     resource_owner_secret=access_token_secret,
# )

# response = oauth.get(
#     "https://api.twitter.com/2/tweets", params=params
# )

# if response.status_code != 200:
#     raise Exception(
#         "Request returned an error: {} {}".format(response.status_code, response.text)
#     )

# print("Response code: {}".format(response.status_code))
# json_response = response.json()
# print(json.dumps(json_response, indent=4, sort_keys=True))