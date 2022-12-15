import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN0ejwEAAAAAG6RofdC3LcMq4iTMeUG%2F2MDWPa4%3DtEZKKeXijG7h4f9BUfdJrMrZy9zKIFAjlrqUldJkZ3VbOrNrYZ"
f = open("hatespeech.txt", "w")

id_list = []
def getIds():
    file = open("ids.txt", "r")
    for sentence in file:
        splitted = sentence.split(",")
        id = splitted[0]
        id_list.append(id)


def create_url(ids):
    tweet_fields = "tweet.fields=lang,author_id"
    idparam = "ids=" + ids
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
    
    for subset in subslist:
        ids = ",".join(subset)
        url = create_url(ids)
        json_response, rep = connect_to_endpoint(url)
        print(json_response)
        print(json.dumps(json_response, indent=4, sort_keys=True))
        for datapiece in json_response["data"]:
            f.write(datapiece["text"] + "\n")


if __name__ == "__main__":
    main()