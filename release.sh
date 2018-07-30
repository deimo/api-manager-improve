#!/bin/bash

if [ $1 ]; then
    git add .
    git commit -m $1
else
    git add .
    git commit -m "update - `date '+%Y-%m-%d %T'`"
fi
git push origin master
git push gnu master

