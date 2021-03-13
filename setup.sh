#!/bin/bash

sudo apt-get update
yes | sudo apt-get upgrade

echo "Installing packages ............................................................"
echo "Installing package: python3-pip ......................"
yes | sudo apt-get install python3-pip
echo "Installing package: speechrecognition ......................"
yes | sudo pip3 install speechrecognition
echo "Installing package: pyaudio ......................"
yes | sudo pip3 install pyaudio
echo "Installing package: wikipedia ......................"
yes | sudo pip3 install wikipedia
echo "Installing sound card: seeed ....................."
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh  --compat-kernel
