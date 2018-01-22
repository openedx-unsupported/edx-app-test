"""
   Module ensure environment level initial settings before starting execution
"""

import os
import datetime
import logging
import logging.handlers
from appium import webdriver
import pytest
from input_data import InputData
from common.globals import Globals
from common import strings
from android.pages.android_new_logistration import AndroidNewLogistration
from ios.pages.ios_new_logistration import IosNewLogistration
from ios.pages.ios_login import IosLogin
from android.pages.android_login import AndroidLogin


@pytest.fixture(scope="session")
def set_capabilities(setup_logging):
    """
    set_capabilities will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests
    """

    log = setup_logging
    globals_contents = Globals(log)
    desired_capabilities = {}
    log.info('- Setting {} capabilities'.format(InputData.target_environment))

    if InputData.target_environment is strings.ANDROID:
        desired_capabilities['platformName'] = strings.ANDROID
        desired_capabilities['platformVersion'] = globals_contents.android_platform_version
        desired_capabilities['deviceName'] = globals_contents.android_device_name
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['appPackage'] = globals_contents.APP_PACKAGE_NAME
        desired_capabilities['appActivity'] = Globals.SPLASH_ACTIVITY_NAME
        desired_capabilities['appWaitActivity'] = Globals.NEW_LOGISTRATION_ACTIVITY_NAME

    elif InputData.target_environment is strings.IOS:
        desired_capabilities['platformName'] = strings.IOS
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        #desired_capabilities['fullReset'] = True
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['bundleId'] = globals_contents.APP_PACKAGE_NAME

    else:
        log.info('{} on - {}'.format(strings.ERROR_SETTING_CAPS, InputData.target_environment))

        return None

    driver = webdriver.Remote(globals_contents.SERVER_URL, desired_capabilities)


    if driver is not None:
        log.info('- Setting {} capabilities are done'.format(InputData.target_environment))

        def fin(request):
            request.addfinalizer(fin)

        return driver
    else:
        log.info('Problem setting {} capabilities'.format(InputData.target_environment))

        return None


@pytest.fixture(scope="session")
def setup_logging():
    current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%S"))

    create_result_directory(strings.RESULTS_DIRECTORY)

    iteration_directory = os.path.join(os.path.dirname(__file__), strings.RESULTS_DIRECTORY,
                                       'Iteration_{}'.format(current_day)
                                       )
    create_result_directory(iteration_directory)

    logs_directory = os.path.join(iteration_directory, "logs")
    create_result_directory(logs_directory)

    # Create Screenshots directory  - will be using in future
    screenshots_directory = os.path.join(iteration_directory, "screenshots")
    create_result_directory(screenshots_directory)

    log_file = os.path.join(os.path.dirname(__file__), logs_directory, strings.LOG_FILE_NAME)

    my_logger = logging.getLogger('edX Logs')
    log_handler = logging.FileHandler(log_file)
    log_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_handler.setFormatter(formatter)
    my_logger.addHandler(log_handler)

    my_logger.info("Logging is successfully set up")

    def fin(request):
        request.addfinalizer(fin)
        my_logger.info("Stopping Logging")
        log_handler.close()

    return my_logger


def create_result_directory(target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)


@pytest.fixture(scope="module")
def login(set_capabilities, setup_logging):
    """
    Login will login user based on env given, it will be reusable in tests
    """

    log = setup_logging
    global_contents = Globals(log)

    if InputData.target_environment == strings.ANDROID:
        android_new_logistration_page = AndroidNewLogistration(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_new_logistration_page.load_app() == Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        assert android_new_logistration_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        log.info('Login screen successfully loaded')
        login_output = android_login_page.login(InputData.login_user_name, InputData.login_password)
        assert login_output == Globals.WHATS_NEW_ACTIVITY_NAME

    elif InputData.target_environment == strings.IOS:
        ios_new_logistration_page = IosNewLogistration(set_capabilities, setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)

        assert ios_new_logistration_page.load_app().text == strings.NEW_LOGIS_DISCOVER_COURSES
        assert ios_new_logistration_page.load_login_screen().text == strings.LOGIN_SCREEN_TITLE
        log.info('Login screen successfully loaded')
        login_output = ios_login_page.login(InputData.login_user_name, InputData.login_password).text

        if global_contents.is_first_time:
            assert login_output == strings.WHATS_NEW_IOS_SCREEN_TITLE
        else:
            assert login_output == strings.MAIN_DASHBOARD_SCREEN_TITLE

        log.info('{} is successfully logged in'.format(InputData.login_user_name))

    return True
