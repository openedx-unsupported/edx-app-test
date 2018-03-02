## edx-app-test
Automated testing for edX Android and iOS mobile applications.

## Installations
- [node](https://nodejs.org/en/)
- [appium](http://appium.io/)
- [pytest](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest-html](https://pypi.python.org/pypi/pytest-html/)


###### iOS(Simulator)
 - Xcode with command line tools
 - [libimobiledevice](http://www.libimobiledevice.org/)
 - [ios_deploy](https://github.com/phonegap/ios-deploy)

**setup for real devices is coming soon**

###### Android(Phone/Tablet/Simulator)
 - [Android SDK](https://developer.android.com/studio/index.html)

 *Don't forget to set environment variables for adb, platfrom-tools etc.*

## Setup
- connect Android Device or start Android/iOS Simulator

- set target_environment in input_data to run on specific environment(default is 'Android'),

    	target_environment = 'iOS' OR 'Android'

- set target_environment version(OS version of specific running device/simulator) in common/globals/ as below,

	    ios_platform_version = '10.3'
	    android_platform_version = '8.0'

- set valid credentials in input_data to login,

        login_user_name = '<username>'
        login_password = '<password>'

- install edx(iOS/Android) app on specific device/simulator


## Run
- Check out the source code

        git clone https://github.com/edx/edx-app-test

- `pytest` - to run all test cases

- `pytest -v <test case name>` to run specific test case

- `pytest -v <test case name> --html=report.html` will create html report
