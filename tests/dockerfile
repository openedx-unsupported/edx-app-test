FROM ubuntu:16.04

WORKDIR /working

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apt-utils \
    usbutils \
    wget \
    curl \
    dialog

#java setup
RUN apt-get install -y openjdk-8-jdk
ENV PATH=$PATH:/usr/lib/jvm/java-8-openjdk/bin

#android setup
RUN wget http://dl.google.com/android/android-sdk_r24.2-linux.tgz
RUN apt-get install android-tools-adb

#nodejs setup
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

#appium setup
RUN npm install appium
EXPOSE 4723
CMD ./node_modules/.bin/appium