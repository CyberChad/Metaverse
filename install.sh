#!/bin/bash

#get prerequisites

sudo apt install git
sudo apt install python-pip

#-- anaconda for linux --
#gui packages
sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

#installer
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh


#soar
sudo apt repository ppa:openjdk-r/ppa
sudo apt update
sudo apt install build-essential swig openjdk-8-jdk python-all-dev

#build soar
cd Soar
python2 scons/scons.py all

#rebuild sml_python so we can call it from our Python 3 environment
sudo apt install python3-dev
python2 scons/scons.py sml_python --python=python3