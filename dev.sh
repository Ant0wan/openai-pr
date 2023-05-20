#!/bin/sh
git diff HEAD^ HEAD | python src/main.py

#gh pr diff <url> --patch | ./main.py
git checkout -b test-pr
echo "echo \"OK\"" > script.sh
git add script.sh
git commit -m "feat(script): test pr first commit"
git push

