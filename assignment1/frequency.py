# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:43:14 2016

@author: vmakri
"""

from __future__ import division
import sys
import json
from collections import Counter


def frequency(tweet_file):
    "string -> dict"
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return Counter(word for tweet in tweets for word in tweet)


if __name__ == '__main__':
    frecuencies = frequency(tweet_file="problem_1_submission.txt")
    total = sum(frecuencies.values())
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), frecuencies[word] / total)
                          for word in frecuencies)