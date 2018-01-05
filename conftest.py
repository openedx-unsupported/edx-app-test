import os
from appium import webdriver
import pytest
from testdata.input_data import InputData
from common.globals import Globals
from common.strings import Strings
from common.elements import Elements

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


@pytest.fixture(scope="session")
def set_capabilities():
    """
    set_caps will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests
    """

    globals_contents = Globals()
    desired_caps = {}
    print('- Setting', InputData.target_environment, 'caps')
    if InputData.target_environment is Strings.ANDROID:
        desired_caps['platformName'] = globals_contents.and_platform
        desired_caps['platformVersion'] = globals_contents.and_platform_version
        desired_caps['deviceName'] = globals_contents.and_device_name
        desired_caps['appWaitDuration'] = '50000'
        desired_caps['appPackage'] = globals_contents.and_app_package_name
        desired_caps['appWaitActivity'] = Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        desired_caps['app'] = PATH(globals_contents.and_app_path)

    elif InputData.target_environment is Strings.IOS:
        desired_caps['platformName'] = globals_contents.ios_platform
        desired_caps['platformVersion'] = globals_contents.ios_platform_version
        desired_caps['deviceName'] = globals_contents.ios_device_name
        #desired_caps['fullReset'] = True
        desired_caps['appWaitDuration'] = '50000'
        #desired_caps['bundleId'] = gl.app_package_name
        desired_caps['app'] = PATH(globals_contents.ios_app_path)

    else:
        print(Strings.ERROR_SETTING_CAPS, ' on - ', InputData.target_environment)
        return None

    driver = webdriver.Remote(globals_contents.appium_remort_url, desired_caps)

    if driver is not None:
        print('- Setting', InputData.target_environment, "caps are done")
        return driver
    else:
        print('Problem setting', InputData.target_environment, "caps")
        return None