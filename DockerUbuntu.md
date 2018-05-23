## Docker Setup for Ubuntu
Dockerize container to execute edx-app-test on Android Phone from Ubuntu Host

## Setup

1- Install followings,

  - [docker](https://www.docker.com/community-edition#/download)
  - [python3](https://www.python.org/downloads/)

2- Install edx Android app on Android Device and connect(specific device)to Ubuntu(through USB) Host

3- Check out/download project source code,

        git clone https://github.com/edx/edx-app-test

4- `ubuntu-setup.sh` script it used to take care of all necessary installation on host, browse project
directory and open `ubuntu-setup.sh` through some editor

   - Enter connected Android Device OS Version against `ANDROID_PLATFORM_VERSION`

   - Enter docker image name in place of <image name> i.e appium-image

   - Enter container name against `--name` i.e `appium-container` and docker image name in place of <image name> as
    defined above, please note that one needs to enter new container name on re-running script

   - Save changes made in `ubuntu-setup.sh`

5- Permit `chmod +x ./ubuntu-setup.sh` and run `./ubuntu-setup.sh`, in terminal, it will start installations and
 return new running container id

6- Run below command and connected android device should be visible under List of devices attached if everything was successful, one may need to re-plug the connected Android Device and run command again, 
           
         docker exec -it $(docker ps -q) adb devices

7- Open another tab of terminal(Ubuntu host) and get the ip of specific running docker container

        docker inspect $(docker ps -q) | grep IPA

8- Pass the above machine ip as server url like below

        export SERVER_URL='http://172.17.0.2:4723/wd/hub'

   its all set to start execution now


## Run

From host machine browse browse project director, and run followings based on your need,

- Execute all test cases in specific directory

        pytest

- Execute specific test case

        pytest -v <test case name>

- Execute specific test case with html report at end

        pytest -v <test case name> --html=report.html


## Execution Next time
After above successful setup one need to follow below steps only for executions next time,

1 - Connect Android Device to host machine

2 - Run Container,  enter container container name against `--name` i.e `appium-container` and docker image name in place of `<image name>` as created earlier

    docker container run -it --privileged --rm -d -p 4723:4723 -v /dev/bus/usb:/dev/bus/usb --name <container name> <image name>

3 - Repeat above step # 6, 7 & 8

4 - execute test cases as mentioned in Run section
