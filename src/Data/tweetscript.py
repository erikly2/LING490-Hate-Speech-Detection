import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN0ejwEAAAAAG6RofdC3LcMq4iTMeUG%2F2MDWPa4%3DtEZKKeXijG7h4f9BUfdJrMrZy9zKIFAjlrqUldJkZ3VbOrNrYZ"

id_list = []
def getIds():
    file = open("ids.txt", "r")
    for sentence in file:
        splitted = sentence.split(",")
        id = splitted[0]
        id_list.append(id)
    #print(id_list)


def create_url():
    tweet_fields = "tweet.fields=lang,author_id"
    getIds()
    subset = id_list[0:99]
    print("subsert")
    print(subset)
    ids = ",".join(subset)
    idparam = "ids=" + ids
    print(ids)
    #ids = "ids=1278747501642657792,1255542774432063488"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?{}&{}".format(idparam, tweet_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()