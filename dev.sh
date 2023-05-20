#!/bin/sh
set -o errexit

FILE='short_commit_sha'
CONTENT="$(git rev-parse --short HEAD)"
ID="$(tr -dc '[:alpha:]' < /dev/urandom | fold -w 1 | head -n 1)$(tr -dc '[:digit:]' < /dev/urandom | fold -w 3 | head -n 1)"
BRANCH="testPR-$ID"

git checkout -b "$BRANCH"
echo "$CONTENT" > "$FILE"

git add "$FILE"
git commit -m "init(pr): add file for test"
git push --set-upstream origin "$BRANCH"

gh pr create --title "[TEST] - PR $ID" --body ""

python src/main.py
gh pr view

git checkout main
gh pr close "$BRANCH" --delete-branch
