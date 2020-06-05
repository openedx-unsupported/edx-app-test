#!/bin/bash

# set `Android' to execute test cases on Android
export TARGET_ENVIRONMENT='Android'

# set Android Version of connected Android Device,
export ANDROID_PLATFORM_VERSION=<android version>

xcode-select --install

pip3 install -r requirements/base.txt

# create a docker-machine
docker-machine create --driver virtualbox <machine name>

# to enable USB in created docker-machine, stop it first
docker-machine stop <machine name>

# allow USB in specific docker-machine
vboxmanage modifyvm <machine name> --usb on --usbehci on

# start specific docker-machine
docker-machine start <machine name>
