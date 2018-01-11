"""
   Module ensure environment level initial settings before starting execution
"""

import os
from appium import webdriver
import pytest
from testdata.input_data import InputData
from common.globals import Globals
from common.strings import Strings

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


@pytest.fixture(scope="session")
def set_capabilities():
    """
    set_capabilities will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests
    """

    globals_contents = Globals()
    desired_capabilities = {}
    print('- Setting', InputData.target_environment, 'caps')
    if InputData.target_environment is Strings.ANDROID:
        desired_capabilities['platformName'] = globals_contents.and_platform
        desired_capabilities['platformVersion'] = globals_contents.and_platform_version
        desired_capabilities['deviceName'] = globals_contents.and_device_name
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['appPackage'] = globals_contents.app_package_name
        desired_capabilities['appActivity'] = Globals.SPLASH_ACTIVITY_NAME
        desired_capabilities['appWaitActivity'] = Globals.NEW_LOGISTRATION_ACTIVITY_NAME

    elif InputData.target_environment is Strings.IOS:
        desired_capabilities['platformName'] = globals_contents.ios_platform
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        #desired_caps['fullReset'] = True
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['bundleId'] = globals_contents.app_package_name
        desired_capabilities['platformName'] = globals_contents.and_platform
        desired_capabilities['platformVersion'] = globals_contents.and_platform_version
        desired_capabilities['deviceName'] = globals_contents.and_device_name
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['appPackage'] = globals_contents.app_package_name
        desired_capabilities['appActivity'] = Globals.SPLASH_ACTIVITY_NAME
        desired_capabilities['appWaitActivity'] = Globals.NEW_LOGISTRATION_ACTIVITY_NAME

    elif InputData.target_environment is Strings.IOS:
        desired_capabilities['platformName'] = globals_contents.ios_platform
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        #desired_capabilities['fullReset'] = True
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['bundleId'] = globals_contents.app_package_name
    else:
        print(Strings.ERROR_SETTING_CAPS, ' on - ', InputData.target_environment)
        return None

    driver = webdriver.Remote(globals_contents.appium_remort_url, desired_capabilities)

    if driver is not None:
        print('- Setting', InputData.target_environment, "caps are done")
        return driver
    else:
        print('Problem setting', InputData.target_environment, "caps")
        return None
