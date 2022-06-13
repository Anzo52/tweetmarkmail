# Python program built with tweepy to get and email a twitter users bookmarks
# Other files in package: config.py and credentials.py


# Importing the necessary modules
import tweepy
import config
import credentials
import time
import datetime
import os
import sys
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Function to get the bookmarks from a twitter user
def get_bookmarks(user, num_bookmarks, start_date, end_date):
    # Get the bookmarks from the user
    bookmarks = api.bookmarks(user, count=num_bookmarks, since=start_date, until=end_date)
    # Return the bookmarks
    return bookmarks


# Function to email the bookmarks
def email_bookmarks(bookmarks, email_address):
    # Create the message
    msg = MIMEMultipart()
    # Set the subject
    msg['Subject'] = "Bookmarks from " + bookmarks[0].user.screen_name + " on " + str(datetime.datetime.now())
    # Set the sender
    msg['From'] = credentials.EMAIL_ADDRESS
    # Set the recipient
    msg['To'] = email_address
    # Set the body
    body = "Here are the bookmarks from " + bookmarks[0].user.screen_name + " on " + str(datetime.datetime.now()) + "\n\n"
    for bookmark in bookmarks:
        body += bookmark.url + "\n"
    msg.attach(MIMEText(body, 'plain'))
    # Send the message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(credentials.EMAIL_ADDRESS, credentials.EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(credentials.EMAIL_ADDRESS, email_address, text)
    server.quit()


# main function
def main():
    # Parse the arguments
    parser = argparse.ArgumentParser(description="Get bookmarks from a twitter user")
    parser.add_argument("-u", "--user", help="The twitter user to get bookmarks from", required=True)
    parser.add_argument("-n", "--num-bookmarks", help="The number of bookmarks to get", type=int, default=100)
    parser.add_argument("-s", "--start-date", help="The start date to get bookmarks from", default="2019-01-01")
    parser.add_argument("-e", "--end-date", help="The end date to get bookmarks from", default="2019-12-31")
    parser.add_argument("-ea", "--email-address", help="The email address to send the bookmarks to", default=credentials.EMAIL_ADDRESS)
    args = parser.parse_args()
    # Get the bookmarks
    bookmarks = get_bookmarks(args.user, args.num_bookmarks, args.start_date, args.end_date)
    # Email the bookmarks
    email_bookmarks(bookmarks, args.email_address)


if __name__ == "__main__":
    main()