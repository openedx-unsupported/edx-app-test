#!/bin/bash

# set `Android' to execute test cases on Android
export TARGET_ENVIRONMENT='Android'

# set Android Version of connected Android Device,
export ANDROID_PLATFORM_VERSION=<android version>

sudo apt update

pip3 install -r requirements/base.txt

docker build -t <image name> .

# Enter container container name against `--name` i.e `appium-container` and docker image name in place of <image name>
# as defined above, it should return new running container id
docker container run -it --privileged --rm -d -p 4723:4723 -v /dev/bus/usb:/dev/bus/usb --name <container name> <image name>
