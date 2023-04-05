#!/usr/bin/env bash
gh pr diff <url> --patch | ./main.py
