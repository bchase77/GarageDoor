#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import fcntl
import time
import sys
import datetime
import CHIP_IO.GPIO as GPIO
import json

from time import gmtime, strftime, sleep
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import TweepError
# import tweepy

from nltk.chat import eliza

print "Hello C.H.I.P. World! Looking at the garage door."

GPIO.cleanup()

chatbot = eliza.Chat(eliza.pairs)

fileout = open("log1.txt", 'w')

fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)

SEVENHOURS = datetime.timedelta(hours=7)
SIXTYSECS = datetime.timedelta(seconds=60)


class Comm:
    """A class which communicates out messages"""

    def __init__(self):
        # enter the corresponding information from your Twitter application:
        # keep the quotes, replace this with your consumer key
        CONSUMER_KEY = 'bCu4uFXpEFBLFmDYs6XaUQ2S1'
        # keep the quotes, replace this with your consumer secret key
        CONSUMER_SECRET = 'CN4pBwVqQL06P7euNCElFj6i6zJUN6diuWD7kXaTl1599pkNNp'
        # keep the quotes, replace this with your access token
        ACCESS_KEY = '777311285138468864-TiZjddKWrzs3FrffnXuUlHT3jynyZEF'
        # keep the quotes, replace this with your access token secret
        ACCESS_SECRET = 'TdbqgAlJA4nRfAm37J3OwbJrG1ed2A1WAYHbN4lznlIW1'

        # auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    def printMaybe(self, text):
        pass  # Do nothing sometimes
        # print text

    def printout(self, text):
        print text

    def tweet(self, text):
        # print text
        try:
            API(self.auth).update_status(text)
        except TweepError as e:
            print e.api_code
            print e.reason
            print e.response
            print e.message
            print e.args
            pass

        print "tweeted" + text

    # To check WiFi:
    #   ip link
    #   sudo ip link set wlan 0 down
    #   sudo ip link set wlan 0 up
    #   nmcli device status
    #
    # def doorOpen(self, duration):
    #     # current_time = strftime("%Y-%m-%d %H:%M:%S:", gmtime())
    #     # current_time = str(int(round((time.time() - SEVENHOURS) * 1000)))
    #     current_time = datetime.datetime.now() - SEVENHOURS
    #     if duration == 0:
    #         message = "Door opened.\r\n"
    #     else:
    #         # message = "Door open for " + str(duration) + " minute.\r\n"
    #         message = "Door open for " + str(duration) + " minute"
    #         if duration > 1:
    #             message = message + "s.\r\n"
    #         else:
    #             message = message + ".\r\n"
    #
    #     # tweepy.API(self.auth).update_status(message)
    #     # API(self.auth).update_status(message)
    #     print message
    #     fileout.write(current_time + message)
    #
    # def doorClosed(self, duration):
    #     # current_time = strftime("%Y-%m-%d %H:%M:%S:", gmtime())
    #     # current_time = str(int(round((time.time() - SEVENHOURS) * 1000)))
    #     current_time = datetime.datetime.now() - SEVENHOURS
    #     # message = "Door closed after " + str(duration) + " minutes.\r\n"
    #     message = "Door closed after " + str(duration) + " minute"
    #     if duration > 1:
    #         message = message + "s.\r\n"
    #     else:
    #         message = message + ".\r\n"
    #     # tweepy.API(self.auth).update_status(message)
    #     # API(self.auth).update_status(message)
    #     print message
    #     fileout.write(current_time + message)
    #
    #     # tweet_api = tweepy.API(self.auth)
    #     # tweet_api = API(self.auth)
    #     # tweet_api.update_status(message)

class Test:
    """A class which can test tweeting"""

    def __init__(self):
        try:
            argfile = str(sys.argv[1])
            filename = open(argfile, 'r')
            f = filename.readlines()
            filename.close()

            for line in f:
                tweet_api.update_status(line)
                time.sleep(300)  # Tweet every 15 minutes
                # time.sleep(900)#Tweet every 15 minutes
                # time.sleep(60)#Tweet every 1 minute
        except:
            print "Test flow. Command line filename of a file with tweets expected but not found."

        # class Sensor:
        # """A class which interfaces to the door sensors"""

        # def __init__(self):
        # Ways to set up GPIOs:
        #
        # Note that events detected in a callback are detected in order,
        # because there is only 1 callback thread.
        # GPIO.setup(door1, GPIO.IN)
        # GPIO.input(door1)
        # GPIO.setup(door1, GPIO.OUT)
        # GPIO.output(door1, GPIO.HIGH)
        # GPIO.remove_event_detect(23)

        # GPIO.setup(door1, GPIO.IN)
        # GPIO.add_event_detect(door1, GPIO.BOTH, bouncetime=500)
        # GPIO.add_event_detect(door1, GPIO.BOTH)


# class StdOutListener(StreamListener):
#     """Handles data received from the stream."""
#     
#     def on_status(self, status):
#         # Prints the text of the tweet
#         text = "Tweet text: " + status.text
#         print text
#       # There are many options in the status object,
#       # hashtags can be very easily accessed.
#         for hashtag in status.entries['hashtags']:
#         print hashtag['text']
#     return true
#
#     def on_data(self, data):
#         # process stream data here
#         print data
#
#         tweet = json.loads(data.strip())
#
#         retweeted = tweet.get('retweeted', False)
#         from_self = tweet.get('user', {}).get('id_str', '') == account_user_id
#
#         if retweeted is not None and not retweeted and not from_self:
#
#             tweetId = tweet.get('id_str')
#             screenName = tweet.get('user').get('screen_name')
#             tweetText = tweet.get('text')
#
#             chatResponse = chatbot.respond(tweetText)
#
#             replyText = '@' + screenName + ' ' + chatResponse
#
#             if len(replyText) > 140:
#                 replyText = replyText[0:137] + '...'
#
#             # twitterApi.update_status(replyText, tweetId)
#             print replyText
#
#     def on_timeout(self):
#         print "Timeout..."
#         return True # To continue listening
#
#     def on_error(self, status):
#         print "Received tweet error, status code: " + status
#         return True # To continue listening
#
# Initialize
# doorState  doorSensor  Timer      Action
# ---------  ----------  -----      ------
# Closed     Closed      don'tCare  do nothing
# Closed     Open        don'tCare  doorState = maybeOpen; Note the time.
# MaybeOpen  Open        < Timeout  do nothing
# MaybeOpen  Open        > Timeout  doorState = open, send message "Door Opened"
# MaybeOpen  Closed      Timer = 0  (Log a shake) doorState = Closed
# Open       Open        If another interval has passed, send message "Door open for N minutes"  
# Open       Closed      don'tCare  doorState = maybeClosed; Note the time.
# MaybeOpen  Closed      < Timeout  do nothing
# MaybeOpen  Closed      > Timeout  doorState = Closed, send message "Door Closed"
# MaybeOpen  Open        Timer = 0  (Log a shake) doorState = Open

door1 = "XIO-P7"

comm = Comm()

count = 0  # Number of intervals the door was noticed open
interval = 1  # Number of minutes to wait between checks for open/closed
door = "closed"

text = "Looking for the door to change now."
print text
comm.tweet(text)

GPIO.setup(door1, GPIO.IN)

# This if __name__ line will only run if this block is pasted
# into the main.py module. 
# if __name__ == '__main__':
streamListener = StdOutListener()
twitterStream = Stream(comm.auth, streamListener)
##fix this: twitterStream.userstream(_with='user')

doorState = 'Closed'  # Start assuming door is closed
# Timeout = 1000 # # of milliseconds door needs to be open to be 'open'
Timeout = 2  # # of seconds door needs to be open to be 'open'
MessageTimeout = 60  # # of seconds between messages while the door is open
maybeOpenTime = 0
openTime = 0
maybeClosedTime = 0
# time.time() == now

while True:
    if doorState == 'Closed':
        if GPIO.input(door1):  # High means sensor is open
            doorState = 'MaybeOpen'
            maybeOpenTime = datetime.datetime.now() - SEVENHOURS
            comm.printMaybe('Closed, maybe open')
        else:  # Sensor is closed
            pass  # do nothing

    elif doorState == 'MaybeOpen':
        if GPIO.input(door1):  # High means sensor is open
            duration = datetime.datetime.now() - SEVENHOURS - maybeOpenTime
            if duration.total_seconds() > Timeout:
                doorState = 'Open'
                openTime = datetime.datetime.now() - SEVENHOURS
                text = "Door opened at " + openTime.strftime("%Y-%m-%d %H:%M:%S:")
                comm.printout(text)
                comm.tweet(text)
            else:  # Door may be open, sensor is still open, no timeout yet
                pass  # do nothing, just wait
        else:  # Sensor is closed
            doorState = 'Closed'
            comm.printMaybe('Shake - now closed')

    elif doorState == 'Open':
        if GPIO.input(door1):  # High means sensor is open
            duration = datetime.datetime.now() - SEVENHOURS - openTime  # now - opened
            if duration.total_seconds() > MessageTimeout:
                count += 1
                text = "Door open for " + str(count) + " minute"
                if count > 1:
                    text += 's.'
                else:
                    text += '.'
                comm.printout(text)
                comm.tweet(text)
                openTime += SIXTYSECS  # Add 60 seconds
            else:  # Duration not long enough, just wait
                pass  # do nothing
        else:  # Sensor is closed
            doorState = "MaybeClosed"
            maybeClosedTime = datetime.datetime.now() - SEVENHOURS
            comm.printMaybe('Open, maybe closed')

    elif doorState == 'MaybeClosed':
        if GPIO.input(door1):  # High means sensor is open
            doorState = 'Open'
            comm.printMaybe('Shake - now Open')
        else:  # Sensor is Closed
            duration = datetime.datetime.now() - SEVENHOURS - maybeClosedTime
            if duration.total_seconds() > Timeout:
                doorState = 'Closed'
                count = 0
                ClosedTime = datetime.datetime.now() - SEVENHOURS
                text = "Door closed at " + ClosedTime.strftime("%Y-%m-%d %H:%M:%S:")
                comm.printout(text)
                comm.tweet(text)
            else:  # Door may be closed, sensor is closed, no timeout yet
                pass  # Do nothing, just wait
    else:  # Error
        comm.printout("This should never print. Statemachine missing state.")

GPIO.cleanup()
fileout.close()
