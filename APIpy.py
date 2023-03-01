import json
import requests as rq

def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")

def load_json(data):
    if not data is None:
        j = json.loads(data)

        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        email = j["results"][0]["email"]

        return fname, lname, email

def main():
    url = "https://randomuser.me/api"

    values = load_json(get_data(url))

    if not values is None:
        print("First Name: ", values[0])
        print("Last Name: ", values[1])
        print("Email: ", values[2])