#!/bin/bash

tput setaf 1; tput bold; echo "WARNING"

tput sgr0

echo "This utility will stop inference process. Continue? (y/n)"

read -p 'y/n: ' uservar
echo

if [ $uservar = 'y' ]
then
  echo "Stopping inference process"
  kill $(ps aux | grep '[p]ython test.py' | awk '{print $2}')
else
  echo "Okay, I won't kill it :)"
fi
