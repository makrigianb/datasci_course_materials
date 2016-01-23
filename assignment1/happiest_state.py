# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:05:24 2016

@author: vmakri
"""

from __future__ import division
import sys
import json
from collections import defaultdict


def read_scores(sent_file):
    "Parse sentiment file, returns a {word: sentiment} dict"
    with open(sent_file) as f:
           d=dict(line.strip().split('\t') for line in f)
           return dict([a, int(x)] for a, x in d.items()) 


def tweet_score(tweet, scores):
    "Returns the score for a tweet or 0 if it's not in AFINN-111.txt"
    return sum(scores.get(word, 0) for word in tweet.split())


def parse(tweet):
    "Extracts country_code, state, text from a tweet"
    try:
        country = tweet['place']['country_code']
        state = tweet['place']['full_name'].split(", ")[1]
        text = tweet['text']
        return country, state, text
    except (KeyError, TypeError, IndexError):
        return None


def happiest_state(tweet_file, sent_scores):
    "Returns the state code of the happiest state in tweet_file"
    n_tweets, scores, happiness = [defaultdict(float) for _ in range(3)]
    with open(tweet_file) as f:
        tweets = (json.loads(line) for line in f)
        parsed_tweets = (parse(tweet) for tweet in tweets if parse(tweet)) # split for efficiecny
        states_scores = ((state, tweet_score(text, sent_scores))
                         for country, state, text in parsed_tweets
                         if len(state) == 2 and country == 'US')

        for state, score in states_scores:
            n_tweets[state] += 1
            scores[state] += score
            happiness[state] = scores[state] / n_tweets[state]
    # Optionally filter by minimum number of tweets to correct for population
    return max(happiness, key=happiness.get)

if __name__ == '__main__':
    scores = read_scores(sent_file="AFINN-111.txt")
    print (happiest_state(tweet_file="three_minutes_tweets.json", sent_scores=scores))