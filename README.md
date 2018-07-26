# edx-app-test
Automated testing for edX Android and iOS mobile applications.

## Using Docker
- [docker for Mac](./DockerMac.md)
- [docker for Ubuntu](./DockerUbuntu.md)

## Manual Installations
- [node](https://nodejs.org/en/)
- [appium](http://appium.io/)
- [pytest](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest-html](https://pypi.python.org/pypi/pytest-html/)


###### iOS(Simulator)
 - Xcode with command line tools
 - [libimobiledevice](http://www.libimobiledevice.org/)
 - [ios_deploy](https://github.com/phonegap/ios-deploy)

###### Android(Phone/Tablet/Simulator)
 - [Android SDK](https://developer.android.com/studio/index.html)

 Don't forget to set environment variables for adb, platform-tools etc.*

#### Setup
- connect/start Android/iOS Device/Simulator

- You will need to configure following system level Environment Variables to run tests against

    - set `Android' to execute test cases on Android or 'iOS' to execute on iOS

          export TARGET_ENVIRONMENT = 'Android'

    - set above selected target_environment's OS Version(of specific running device/simulator) like below

          export ANDROID_PLATFORM_VERSION = '8.0'

          export IOS_PLATFORM_VERSION = '11.2'

    - set valid credentials to login

          export LOGIN_USER_NAME = '<username>'

          export LOGIN_PASSWORD = '<password>'

    - set server url

          export SERVER_URL = 'http://localhost:4723/wd/hub'

- install edx(iOS/Android) app on specific device/simulator


#### Run
- Check out/download the source code, browse its directory

        git clone https://github.com/edx/edx-app-test

- `pytest` - to run all test cases

- `pytest -v <test case name>` to run specific test case

- `pytest -v <test case name> --html=report.html` will create html report
