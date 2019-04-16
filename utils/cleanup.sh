#!/bin/bash

tput setaf 1; tput bold; echo "WARNING"

tput sgr0

echo "This utility will erase every image captured so far. Continue? (y/n)"

read -p 'y/n: ' uservar
echo

if [ $uservar = 'y' ]
then
  echo "Erasing all files in /home/nvidia/results/"
  rm -rf /home/nvidia/results/.*jpg
else
  echo "Okay, I won't erase anything"
fi
