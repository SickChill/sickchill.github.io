#!/bin/bash -
# Copy to SR dir, ./genchanges.sh > path/to/sickrage.github.io/sickrage-news/CHANGES.md
for i in `git tag --sort=-refname`; do
  echo '###' $i
  echo ''
  prev=$(git log $i^ | head -n1 | sed 's/\(commit \|(.*$\)//g')
  echo '[full changelog](https://github.com/SickRage/SickRage/compare/'$prev'...'$i')'
  echo ''
  git cat-file tag $i | tail -n+6 | sed 's/^/* /g' | sed '/-----BEGIN PGP SIGNATURE-----/,+9 d'
  echo ''
done
