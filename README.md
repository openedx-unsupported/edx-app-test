## edx-app-test
Automated testing for edX Android and iOS mobile applications.

###Setup
Install followings.  
- [node](https://nodejs.org/en/)
- [appium](http://appium.io/)
- [pytest](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest-html](https://pypi.python.org/pypi/pytest-html/)


####iOS(Simulator)
Install followings to setup iOS environment, 
 
 - Xcode with command line tools
 - [libimobiledevice](http://www.libimobiledevice.org/)
 - [ios_deply](https://github.com/phonegap/ios-deploy)
 
setup for real devices is coming soon

####Andorid(Phone/Tablet/Simulator)
Install following to setup Android environment, 

 - [setup Android SDK](https://developer.android.com/studio/index.html)
 - Don't forget to set environment variables for adb, platfrom-tools 

 Andorid(Phone/Tablet/Simulator)
 - node
 - appium
 - pytest
 - Android SDK

###Run 

- set target_environment from /testdata/input_data to "Android" or "iOS" to run on specific environment

- Connect Android Device/load Android Simulator/iOS Simulator

- clone/download project and browse to the root dir


- `pytest` - to run all test cases 


- `pytest -v <test case name>` to run specific test case 



- `pytest -v <test case name> --html=report.html` will create html report