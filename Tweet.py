#!/usr/bin/env python
#The class for project on datamining large sets of data from file
#Caden MacKenzie

__author__ = "Caden MacKenzie"
__file__ = "tweets.csv"
__version__ = "1.0"

class Tweet:
    
    def __init__(self, data_):
        '''Initialize variables associated with a new line'''
        self.data = data_
    
    def average1(self):
        '''Calculates the average characters in a tweet in the list'''
        sum_1 = 0
        text = []
        counter = 0
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            chars = len(text[i])
            sum_1 = sum_1 + chars
            counter = counter + 1
        average = sum_1/counter
        print "Average length of the tweets: "
        print average
    
    
    def hashtags(self):
        '''Searches every tweet for the # symbol and adds to counters'''
        sum_1 = 0.0
        text = []
        counter = 0.0
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            if text[i].find('#') != -1:
                sum_1 += 1
            counter +=1
        hashtags =  (sum_1/counter)*100
        print "The percent of tweets with a # is "
        print hashtags
    
    def atsign(self):
        '''Finds the number of times the # is used in tweets'''
        sum_1 = 0.0
        text = []
        counter = 0.0
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            if text[i].find('@') != -1:
                sum_1 += 1
            counter +=1
        hashtags =  (sum_1/counter)*100
        print "The percent of tweets with a @ is "
        print hashtags
               

    def givenword(self, word):
        '''Takes a word as input from the user, searches all tweets for the word'''
        sum_1 = 0
        text = []
        counter = 0.0
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            if text[i].find(word) != -1:
                sum_1 += 1
            counter += 1
        wordpercent = (sum_1/counter)*100
        print "The percent of tweets with this word is: "
        print wordpercent
    
    def punctuation(self):
        '''Searches all the tweets for punctuation, find percent without'''
        punctuation = set("@")
        counter = 0.0
        numberwithout = 0.0
        text = []
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            #print type(individtext[1])
            #print individtext[0]
        for word in text:
            if punctuation & set(word):
                numberwithout += 1
            counter += 1
        percent = (numberwithout/counter)*100
        percent2 = 100-percent
        print "The percent of tweets without punctuation is: "
        print percent2
            
    
    def longest(self):
        '''Finds longest word'''
        word = ""
        current = []
        text = []
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            individtext = text[i].split(" ")
            for j in range(len(individtext)):
                if len(individtext[j]) > len(word):
                    word = individtext[j]
        print "The longest word in the list of tweets is: "
        print word
        
    def dictionary(self):
        '''Finds the 100 most used words in all the tweets'''
        my_dictionary = {}
        text = []
        for i in range(len(self.data)):
            text.append(self.data[i][5])
            individtext = text[i].split(" ")
            for word in individtext:
                if word in my_dictionary:
                    my_dictionary[word] += 1
                else:
                    my_dictionary[word] = 1
        popular_words = sorted(my_dictionary, key = my_dictionary.get, reverse = True)
        top = popular_words[:100]
        print "The top one hundred words in the list is "
        print top
        #print my_dictionary
        #google search: find most popular word in a list python
        #got help from Johnsyweb's answer
        #http://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list
           
            
    def commonwords(self):
        '''Finds top words that are in positive tweets but not in negative tweets'''
        uncommon_dictionary = {}
        positive_dictionary = {}
        negative_dictionary = {}
        text_pos = []
        text_neg = []
        for i in range(len(self.data)):
            if self.data[i][0] == 4:
                text_pos.append(self.data[i][5])
                individ_pos = text_pos[i].split(" ")
                if word in individ_pos:
                    positive_dictionary[word] += 1
                else:
                    positive_dictionary[word] = 1
            if self.data[i][0] == 0:
                text_neg.append(self.data[i][5])
                individ_neg = text_neg[i].split(" ")
                if word in individ_neg:
                    negative_dictionary[word] += 1
                else:
                    negative_dictionary[word] = 1
    
        
    def topuser(self):
        '''Finds top user using a dictionary'''
        my_dictionary = {}
        text = []
        for i in range(len(self.data)):
            text.append(self.data[i][4])
            for word in text:
                if word in my_dictionary:
                    my_dictionary[word] += 1
                else:
                    my_dictionary[word] = 1
        top_users = sorted(my_dictionary, key = my_dictionary.get, reverse = True)
        top = top_users[:1]
        print "The user with the most tweets: "
        print top
        
    def averagetweetper(self):
        '''Finds the average number of tweets per user'''
        my_dictionary = {}
        text = []
        counter = 0.0
        for i in range(len(self.data)):
            text.append(self.data[i][4])
            counter += 1
            for word in text:
                if word in my_dictionary:
                    my_dictionary[word] += 1
                else:
                    my_dictionary[word] = 1
        total = len(my_dictionary)
        average = total/counter
        print "The average tweets per user is: "
        print average
    
    
    def singlehour(self):
        '''Finds the hour in which people post the most tweets'''
        my_dictionary = {}
        text = []
        time= []
        for i in range(len(self.data)):
            text.append(self.data[i][2])
            individtext = text[i].split(" ")
            for j in range(len(individtext)):
                hour_sec = individtext[3].split(":")
                time.append(hour_sec[0])
            for word in time:
                if word in my_dictionary:
                    my_dictionary[word] += 1
                else:
                    my_dictionary[word] = 1
        popular_words = sorted(my_dictionary, key = my_dictionary.get, reverse = True)
        top_hour = popular_words[:1]
        print "The most popular hour to tweet is: "
        print top_hour
        
        
        
        
        
        
    
 
 
 
 
    
   
