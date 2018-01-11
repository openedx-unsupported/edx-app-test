## edx-app-test
Automated testing for edX Android and iOS mobile applications.

#### Installations
- [node](https://nodejs.org/en/)
- [appium](http://appium.io/)
- [pytest](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest-html](https://pypi.python.org/pypi/pytest-html/)


###### iOS(Simulator) 
 - Xcode with command line tools
 - [libimobiledevice](http://www.libimobiledevice.org/)
 - [ios_deply](https://github.com/phonegap/ios-deploy)
 
setup for real devices is coming soon

###### Andorid(Phone/Tablet/Simulator)
 - [Android SDK](https://developer.android.com/studio/index.html)
 - Don't forget to set environment variables for adb, platfrom-tools etc.
 
#### Setup  
- Start Android Device/Simulator/iOS Simulator
- set target_environment in /testdata/input_data either "Android" or "iOS" to run on specific environment(default is 'iOS')


    target_environment = 'iOS'
    OR
    target_environment = 'Android'

 - [Android SDK](https://developer.android.com/studio/index.html)
 - Don't forget to set environment variables for adb, platfrom-tools etc.
- set target_environment version(OS version of specific running device/simulator) in common/globals/ as below, 


	ios_platform_version = '10.3'
	 OR 
	and_platform_version = '8.0'

- set valid credentials in /testdata/input_data to login


	 login_user_name = '<username>'
     login_password = '<password>'

- install edx(iOS/Android) app on specific device/simulator 


#### Run 
- set target_environment in /testdata/input_data either "Android" or "iOS" to run on specific environment
- set valid credentials in /testdata/input_data to login
- Connect Android Device/load Android Simulator/iOS Simulator
- install edx (iOS/Android) app on specific device/simulator
- clone/download test project and browse to the root dir

- `pytest` - to run all test cases
- `pytest -v <test case name>` to run specific test case

- `pytest -v <test case name> --html=report.html` will create html report 