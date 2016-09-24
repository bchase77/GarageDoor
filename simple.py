#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CHIP_IO.GPIO as GPIO
import tweepy, time, sys
from time import gmtime, strftime

print "Hello C.H.I.P. World! Looking at XIO-P7. "

#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
#keep the quotes, replace this with your consumer key
CONSUMER_KEY = 'bCu4uFXpEFBLFmDYs6XaUQ2S1'
#keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = 'CN4pBwVqQL06P7euNCElFj6i6zJUN6diuWD7kXaTl1599pkNNp'
#keep the quotes, replace this with your access token
ACCESS_KEY = '777311285138468864-TiZjddKWrzs3FrffnXuUlHT3jynyZEF'
#keep the quotes, replace this with your access token secret
ACCESS_SECRET = 'TdbqgAlJA4nRfAm37J3OwbJrG1ed2A1WAYHbN4lznlIW1'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
tweet_api = tweepy.API(auth)

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#for line in f:
    #tweet_api.update_status(line)
    #time.sleep(300)#Tweet every 15 minutes
    ##time.sleep(900)#Tweet every 15 minutes
    ##time.sleep(60)#Tweet every 1 minute

# Initialize
# Read gpios
# If door open, send a tweet
# If timer timed out then send a tweet

door1 = "XIO-P7"

# Ways to set up GPIOs:
#
# Note that events detected in a callback are detected in order,
# because there is only 1 callback thread.
#GPIO.setup(door1, GPIO.IN)
#GPIO.input(door1)
#GPIO.setup(door1, GPIO.OUT)
#GPIO.output(door1, GPIO.HIGH)
#GPIO.remove_event_detect(23)

GPIO.setup(door1, GPIO.IN)
#GPIO.add_event_detect(door1, GPIO.BOTH)
GPIO.add_event_detect(door1, GPIO.BOTH, bouncetime=500)

print 0
def my_callback(self):
  print "Event!!"
  current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  GPIO_Level = GPIO.input(door1)
  message = current_time + "  " + str(GPIO_Level)
  tweet_api.update_status(message)
  print message

print 1
GPIO.add_event_callback(door1, my_callback)
print 2

while True:
  print 3
  GPIO.wait_for_edge(door1, GPIO.FALLING)
  print "Door down"

  print 4
  GPIO.wait_for_edge(door1, GPIO.RISING)
  print "Door up"

  input("Press enter to end")

  choice = raw_input("Enter 'b' to quit")
  if choice == 'b' :
    print "You win"
    break

GPIO.cleanup()

