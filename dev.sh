#!/bin/sh
git diff HEAD^ HEAD | python src/main.py

#gh pr diff <url> --patch | ./main.py
