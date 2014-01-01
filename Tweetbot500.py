# This script relies on https://github.com/bear/python-twitter

# Written by TronLaser on GitHub
# Report bugs to github.com/tronlaser

import twitter
import ConfigParser
import time
from time import gmtime, strftime
import random

print ("Everything imported fine")

config = ConfigParser.ConfigParser()
config.read("config.ini")
consumer_key = config.get('login', 'consumer_key')
consumer_secret = config.get('login', 'consumer_secret')
access_token_key = config.get('login', 'access_token_key')
access_token_secret = config.get('login', 'access_token_secret')

print ("Config file found and read")
print ("Connecting to the API")

api = twitter.Api(consumer_key,consumer_secret,access_token_key,access_token_secret)
test = api.VerifyCredentials()

if test == "":
    print ("Connection failed. Check your details")
else:
    print ("Connection successful!")

print ("READY!")

# Below is the data for my tweetbot
# Erase the stuff below and make what you want

listoftweets = ['No', 'Nope', 'Negative', 'Nah', 'Not yet', 'Still no', 'Nyet', 'Nein', 'Nerp'] # The list of possible tweets

def post(): # This will pick a message at random and tweet it
    tweet = random.choice(listoftweets)
    status = api.PostUpdate(tweet)
    print status.text

while True: # This is the main loop for the program
    ctime = strftime("%M", gmtime())
    if ctime == "15":
        post()
    elif ctime == "30":
        post()
    elif ctime == "45":
        post()
    elif ctime == "00":
        post()
    time.sleep(60)

