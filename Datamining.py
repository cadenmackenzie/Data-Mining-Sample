#!/usr/bin/env python
#DataminingFunctions
#This program runs datamining tests on a given set of data

#Caden MacKenzie
#A tweet class is imported for use of its methods

from Tweet import Tweet

my_file = open("200tweets.csv", "r")
print type(my_file)
data = []

for line in my_file:
    data.append(tuple(line.strip().split(',')))

my_tweet = Tweet(data)
my_tweet.average1()
my_tweet.hashtags()
my_tweet.atsign()
given_word = raw_input("Please enter a word to search for: ")
my_tweet.givenword(given_word)
my_tweet.longest()
my_tweet.punctuation()
my_tweet.dictionary()
my_tweet.topuser()
my_tweet.averagetweetper()
my_tweet.singlehour()


my_file.close()

