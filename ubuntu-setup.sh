#!/bin/bash

# set `Android' to execute test cases on Android
export TARGET_ENVIRONMENT='Android'

# set Android Version of connected Android Device,
export ANDROID_PLATFORM_VERSION='9'

sudo apt update

pip3 install -r requirements/base.txt

docker build -t appium-image .

# Enter container container name against `--name` i.e `appium-container` and docker image name in place of <image name>
# as defined above, it should return new running container id
docker container run -it --privileged --rm -d -p 4723:4723 -v /dev/bus/usb:/dev/bus/usb --name appium-container appium-image
