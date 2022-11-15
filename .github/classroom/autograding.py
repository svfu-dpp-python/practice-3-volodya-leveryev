#!/usr/bin/python

import os

# 1. git log
found = False
extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png']
for f in os.listdir('1_log'):
    for e in extensions:
        if f.lower().endswith(e):
            found = True
            break
if not found:
    print("Screenshot after 'git log' not found")
    exit(-1)

# 2. git commit --amend
with open('2_commit_amend/begin.txt') as f:
    _, hash1 = f.readline().split()
with open('2_commit_amend/end.txt') as f:
    _, hash2 = f.readline().split()
if hash1 == hash2:
    print("Hashes before and after 'git commit --amend' must differ")
    exit(-1)

# 3. git restore --staged
msg1 = "Changes to be committed"
msg2 = "Changes not staged for commit"
with open('3_restore/begin.txt') as f:
    status1 = f.read()
with open('3_restore/end.txt') as f:
    status2 = f.read()
if msg1 in status2:
    print("Incorrect log before 'git reset --staged'")
    exit(-1)
if msg2 in status1:
    print("Incorrect log after 'git reset --staged'")
    exit(-1)
