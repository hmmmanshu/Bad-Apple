#!/bin/bash

# checking if python3 is installed
if [[ ! "$(python3 -V)" =~ "Python 3" ]]; then
    echo "Python 3 is not installed."
    exit 1;
fi

# installing other required packages
echo "Installing numpy..."
pip3 install numpy
echo "Installing imutils..."
pip3 install imutils
echo "Installing opencv..."
pip3 install opencv-python

python3 ./BadApple.py --video videos/videoplayback.m4v