#!/usr/bin/python

import os

# 1. git log
extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png']
for f in os.listdir('1_log'):
    for e in extensions:
        if f.lower().endswith(e):
            break
else:
    print('Screenshot after "git log" not found')
    exit(-1)

# 2. git commit --amend
with open('2_commit_amend/begin.txt') as f:
    _, hash1 = f.readline().split()
with open('2_commit_amend/end.txt') as f:
    _, hash2 = f.readline().split()
if hash1 == hash2:
    print('Hashes before and after "git commit --amend" must differ')
    exit(-1)
