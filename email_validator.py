#!/usr/bin/env python
import re

pattern = re.compile("([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{1,3})")

num_emails = int(raw_input("how many emails?\n"))

emails_cands = []
for _ in xrange(num_emails):
    emails_cands.append(raw_input("Input email:\n"))

def is_email(email):
    if pattern.match(email):
        return True
    else:
        return False

emails = filter(is_email, emails_cands)

print emails