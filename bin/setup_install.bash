#!/bin/bash
# run chmod +x ./bin/{filename}
# this is for Mac with M1 chip

# Stop on errors
set -Eeuo pipefail

# echo on
set -x

# install python
# arch -x86_64 brew install python3

# run this once
python3 -m venv env
# source into the environment with
source env/bin/activate

# update pip
pip install --upgrade pip

# install node
arch -x86_64 brew install node

# install wget
arch -x86_64 brew install wget

# get requirements.txt and install contents
pip install -r requirements.txt

# install python tools and html5 validator
pip install --upgrade pip setuptools wheel
pip install html5validator

# install python
pip install pycodestyle
pip install pydocstyle
pip install pylint

# install python debugger
pip3 install pdbpp

# install flask
pip install Flask

# install SQLite and REST API tools
arch -x86_64 brew install sqlite3 curl httpie coreutils

# THIS IS OPTIONAL - install chrome and drivers
# arch -x86_64 brew install --cask google-chrome
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
# npm install chromedriver --detect_chromedriver_version --no-save
# npm chromedriver --version


# check versions
echo ""
echo "Make sure you are in your virtual environemnt, check if PATH ends with /env/"
echo $VIRTUAL_ENV
python3 --version
html5validator --version
sqlite3 --version
curl --version
http --version
node --version
npm --version