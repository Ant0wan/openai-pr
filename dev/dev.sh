#!/bin/sh
set -o errexit
# shellcheck source=env-01.sh
. "$1"

FILE='short_commit_sha'
CONTENT="$(git rev-parse --short HEAD)"
ID="$(tr -dc '[:alpha:]' < /dev/urandom | fold -w 1 | head -n 1)$(tr -dc '[:digit:]' < /dev/urandom | fold -w 3 | head -n 1)"
export GITHUB_BRANCH="testPR-$ID"

git checkout -b "$GITHUB_BRANCH"
echo "$CONTENT" > "$FILE"
git add "$FILE"
git commit -m "init(pr): add file for test"
git push --set-upstream origin "$GITHUB_BRANCH"
gh pr create --title "[TEST] - PR $ID" --body ""
python src/main.py
gh pr view
sleep 5
git checkout main
gh pr close "$GITHUB_BRANCH" --delete-branch
