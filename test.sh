#!/usr/bin/env bash
gh pr diff <url> --patch | ./main.py

git diff HEAD^ HEAD | ./main.py
