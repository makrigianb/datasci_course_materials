# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:43:00 2016

@author: vmakri
"""


from __future__ import division
import sys
import json


def read_scores(sent_file):
    with open(sent_file) as f:
            d=dict(line.strip().split('\t') for line in f)
            return dict([a, int(x)] for a, x in d.items()) 


def score_tweet(tweet, scores):
    return sum(int(scores.get(word, 0)) for word in tweet)


def unknown_word_scores(tweet_file, scores):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return {word: score_tweet(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores}


if __name__ == '__main__':
    sent_file =  "AFINN-111.txt"    #sys.argv[1]#
    tweet_file =  "problem_1_submission.txt"   #sys.argv[2]#
    scores = read_scores(sent_file=sent_file)
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in unknown_word_scores(
                              tweet_file=tweet_file,
                              scores=scores).items())