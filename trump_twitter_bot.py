#! /usr/bin/env python
from copy import deepcopy
from unittest import TestCase
from pprint import pprint

""" Implement dfs to find the longest sequence of Trump-Person responses """


def dfs(start, result=[], limit=-1):
    start_dict = {"sender": start['sender'], "message": start['message']}
    result.append(start_dict)
    for reply in start['replies']:
        result.append({"sender": reply['sender'], "message": reply['message']})

    return result


sample_convo = {
    "sender": "realdonaldtrump",
    "message": "freedom",
    "replies": [{"sender": "twitter_user", "message": "you moron", "replies": {}}]}

sample_result = [{"sender": "realdonaldtrump", "message": "freedom"},
                 {"sender": "twitter_user", "message": "you moron"}]

sample_convo2 = {'message': 'level 1',
                 'replies': [{'message': 'level 2',
                              'replies': [{'message': 'level 3',
                                           'replies': [{'message': 'level 4',
                                                        'replies': {},
                                                        'sender': 'twitter_user'}],
                                           'sender': 'realdonaldtrump'}],
                              'sender': 'twitter_user'}],
                 'sender': 'realdonaldtrump'}

sample_result2 = [{"sender": "realdonaldtrump", "message": "level 1"},
                  {"sender": "twitter_user", "message": "level 2"}, {
                      "sender": "realdonaldtrump", "message": "level 3"},
                  {"sender": "twitter_user", "message": "level 4"}]

if __name__ == '__main__':
    print list(dfs(sample_convo)) == sample_result
    print list(dfs(sample_convo2)) == sample_result2
