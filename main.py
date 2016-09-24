#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import fcntl
import time
import sys

from time import gmtime, strftime, sleep
import CHIP_IO.GPIO as GPIO
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from nltk.chat import eliza

print "Hello C.H.I.P. World! Looking at the garage door."

GPIO.cleanup()

chatbot = eliza.Chat(eliza.pairs)

fileout = open("log1.txt", 'w')

fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)

class Comm:
  """A class which communicates out messages"""

  def __init__(self):
    #enter the corresponding information from your Twitter application:
     #keep the quotes, replace this with your consumer key
    CONSUMER_KEY = 'bCu4uFXpEFBLFmDYs6XaUQ2S1'
     #keep the quotes, replace this with your consumer secret key
    CONSUMER_SECRET = 'CN4pBwVqQL06P7euNCElFj6i6zJUN6diuWD7kXaTl1599pkNNp'
     #keep the quotes, replace this with your access token
    ACCESS_KEY = '777311285138468864-TiZjddKWrzs3FrffnXuUlHT3jynyZEF'
     #keep the quotes, replace this with your access token secret
    ACCESS_SECRET = 'TdbqgAlJA4nRfAm37J3OwbJrG1ed2A1WAYHbN4lznlIW1'

    self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

  def doorOpen(self, duration):
    #current_time = strftime("%Y-%m-%d %H:%M:%S:", gmtime())
    current_time = str(int(round(time.time()*1000)))
    if duration == 0:
      message = "Door opened.\r\n"
    else:
      message = "Door open for " + str(duration) + " minutes.\r\n"

    #tweepy.API(self.auth).update_status(message)
    #API(self.auth).update_status(message)
    print message
    fileout.write(current_time + message)


  def doorClosed(self, duration):
    #current_time = strftime("%Y-%m-%d %H:%M:%S:", gmtime())
    current_time = str(int(round(time.time()*1000)))
    message = "Door closed after " + str(duration) + " minutes.\r\n"
    #tweepy.API(self.auth).update_status(message)
    #API(self.auth).update_status(message)
    print message
    fileout.write(current_time + message)

    #tweet_api = tweepy.API(self.auth)
    #tweet_api = API(self.auth)
    #tweet_api.update_status(message)

class Test:
  """A class which can test tweeting"""

  def __init():
    try:
      argfile = str(sys.argv[1])
      filename=open(argfile,'r')
      f=filename.readlines()
      filename.close()
  
      for line in f:
        tweet_api.update_status(line)
        time.sleep(300)#Tweet every 15 minutes
        ##time.sleep(900)#Tweet every 15 minutes
        ##time.sleep(60)#Tweet every 1 minute
    except: 
      print "Test flow. Command line filename of a file with tweets expected but not found."

#class Sensor:
  #"""A class which interfaces to the door sensors"""

  #def __init__(self):
    # Ways to set up GPIOs:
    #
    # Note that events detected in a callback are detected in order,
    # because there is only 1 callback thread.
    #GPIO.setup(door1, GPIO.IN)
    #GPIO.input(door1)
    #GPIO.setup(door1, GPIO.OUT)
    #GPIO.output(door1, GPIO.HIGH)
    #GPIO.remove_event_detect(23)
    
    #GPIO.setup(door1, GPIO.IN)
    #GPIO.add_event_detect(door1, GPIO.BOTH, bouncetime=500)
    #GPIO.add_event_detect(door1, GPIO.BOTH)

class ReplyToTweet(StreamListener):
 
  def on_data(self, data):
    # process stream data here
    print data

    tweet = json.loads(data.strip())
   
    retweeted = tweet.get('retweeted', False)
    from_self = tweet.get('user',{}).get('id_str','') == account_user_id

    if retweeted is not None and not retweeted and not from_self:

      tweetId = tweet.get('id_str')
      screenName = tweet.get('user').get('screen_name')
      tweetText = tweet.get('text')

      chatResponse = chatbot.respond(tweetText)

      replyText = '@' + screenName + ' ' + chatResponse

      if len(replyText) > 140:
        replyText = replyText[0:137] + '...'

      #twitterApi.update_status(replyText, tweetId)
      print replyText

    def on_error(self, status):
      print status

#def on_data(self, data): # When a tweet comes in, on_data processes it

# Initialize
# Read gpios
# If door open, send a tweet
# If timer timed out then send a tweet

door1 = "XIO-P7"

comm = Comm()

count = 0 # Number of intervals the door was noticed open
interval = 1 # Number of minutes to wait between checks for open/closed
door = "closed"

print "Looking for the door to change now."

GPIO.setup(door1, GPIO.IN)

# This if __name__ line will only run if this block is pasted
# into the main.py module. 
#if __name__ == '__main__':
streamListener = ReplyToTweet()
twitterStream = Stream(comm.auth, streamListener)
twitterStream.userstream(_with='user')

# Look for user input to clean up gracefully

#try:
  #while True:
    #stdin = sys.stdin.read()
    #if "\n" in stdin or "\r" in stdin:
      #break
  
    #Every qty of minutes, check status
    #If open then send a message with count of open time 
    #If closed then reset the open counter

while True:
  if GPIO.input(door1): # High means it's open
    if door is "AlreadyOpen":
      #print 1
      pass
    else:
      #print 2
      door = "AlreadyOpen"
      print "Door opened"
      comm.doorOpen(count * interval)
      count = count + 1
      #sleep(interval * 60) # sleep is seconds; interval is minutes
      #sleep(interval * 2) # Short intervals for testing
  else: # Door is now closed
    #print 3
    if door is "AlreadyOpen":
      #print 4
      print "Door closed"
      door = "closed"
      comm.doorClosed(count * interval)
      count = 0

#except IOError as e:
  #print "Exception"
  #print e.errorno e.strerror
  #GPIO.cleanup()
  #fileout.close()
  #pass

GPIO.cleanup()
fileout.close()

