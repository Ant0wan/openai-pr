#!/bin/sh
set +x
git add --all
git commit -m "test"
git push
NEWTAG="0.0$(echo "$(git tag | sort -V | tail -n1 | cut -d '.' -f2,3) + 0.01" | bc)"
git tag "$NEWTAG"
git push --tag
gh release create "$NEWTAG" --title "$NEWTAG" --notes ""
