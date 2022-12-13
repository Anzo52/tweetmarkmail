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
    """
    > The function `cli_auth_api` takes four arguments (consumer_key, consumer_secret, access_token,
    access_token_secret) and returns an object that can be used to make requests to the Twitter API
    
    :param consumer_key: The API key generated when you registered your app
    :param consumer_secret: The consumer secret key for your app
    :param access_token: The access token you get from the API
    :param access_token_secret: The access token secret provided by Twitter when you registered your
    application
    :return: An object that represents the Twitter API.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def termen(opts):
    """
    It takes a list of strings and returns the string that the user selects from a menu
    
    :param opts: a list of strings, each string is a menu entry
    :return: The index of the selected option.
    """
    term_menu = simple_term_menu.Menu(opts)
    menu_entry_index = term_menu.show()
    return opts[menu_entry_index]

def start_menu():
    """
    It displays a menu with three options, and then calls the appropriate function based on the user's
    choice
    """
    menu_items = [
        "Config/Keys", 
        "Main", 
        "Exit"
        ]
    choice = termen(menu_items)
    if choice == menu_items[0]:
        config_menu()
    elif choice == menu_items[1]:
        main_menu()
    else:
        exit()

# TODO: config_menu()
def config_menu():
    pass

# TODO: main_menu()
def main_menu():
    pass

if __name__ == "__main__":
    start_menu()