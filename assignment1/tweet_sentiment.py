# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import json


def read_scores(sent_file):
    "Parse sentiment file, returns a {word: sentiment} dict"
    with open(sent_file) as f:
        d=dict(line.strip().split('\t') for line in f)
        return dict([a, int(x)] for a, x in d.items()) 
        #return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}#


def tweet_score(tweet, scores):
    "Returns the score for a tweet or 0 if it's not in AFINN-111.txt"
    return sum(scores.get(word, 0) for word in tweet.split())


def tweet_scores(tweet_file, scores):
    "Calculate scores for all tweets in tweet_file"
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '') for line in f)
        return [tweet_score(tweet, scores) for tweet in tweets]


if __name__ == '__main__':
    sent_file =  "AFINN-111.txt"    #sys.argv[1]#
    tweet_file =  "problem_1_submission.txt"   #sys.argv[2]#
    scores = read_scores(sent_file=sent_file)
    sys.stdout.writelines('{0}.0\n'.format(score)
                          for score in tweet_scores(tweet_file=tweet_file, scores=scores))
