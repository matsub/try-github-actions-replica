#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import json
import os
import random
import urllib.request
import urllib.parse

MAX_REVIEWER = os.environ.get('MAX_REVIEWER')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

def create_github_request(url, data=None):
    req = urllib.request.Request(url, data)
    req.add_header('Authorization', f'token {GITHUB_TOKEN}')
    return req


# open event.json
with open(os.environ.get('GITHUB_EVENT_PATH')) as f:
    event = json.load(f)
    pr_event = event["pull_request"]

status_endpoint = pr_event["_links"]["statuses"]
reviewers = pr_event["requested_reviewers"]


# quit if reviewers are enough
if len(reviewers) >= int(MAX_REVIEWER):
    exit(78)


collaborators_endpoint = event["repository"]["collaborators_url"].split("{")[0]

req = create_github_request(collaborators_endpoint)
with urllib.request.urlopen(req) as response:
    res = json.load(response)
    new_reviewer = random.choice(res)

    reviewers.append(new_reviewer)

    reviewers_name = map(lambda x: x["login"], reviewers)

    # POST /repos/:owner/:repo/pulls/:number/requested_reviewers
    url = f'{pr_event["url"]}/requested_reviewers'
    body = { "reviewers": list(reviewers_name), "team_reviewers": [] }
    data = json.dumps(body).encode()
    print(body)

    req = create_github_request(url, data)
    req.add_header('Content-Type', 'application/json')

    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as err:
        print(err.read())

exit()
