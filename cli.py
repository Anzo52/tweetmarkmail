# Command line interface for tweepy_bookmarks

from tweepy_bookmarks import get_bookmarks as get_bookmarks
from tweepy_bookmarks import email_bookmarks as email_bookmarks
import tweepy
import simple_term_menu

# get config and credentials
# credentials: consumer key, consumer secret, access token, access token secret
# config options: user to get bookmarks from, num of bookmarks, start/end date, address to send bookmarks, sleep time
# get_bookmarks(user, num_bookmarks, start date, end date) -> bookmarks, email_bookmarks(bookmarks, email address)
# set auth

def cli_auth_api(consumer_key, consumer_secret, access_token, access_token_secret): 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
