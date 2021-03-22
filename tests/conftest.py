# coding=utf-8
"""
   Module ensure environment level initial settings before starting execution
"""

import datetime
import logging.handlers
import os

import pytest
from appium import webdriver

from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_new_landing import IosNewLanding


# pylint: disable=redefined-outer-name
@pytest.fixture(scope="session")
def set_capabilities(setup_logging):
    """
    set_capabilities will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests

    Arguments:
            setup_logging (logger): logger object

    Returns:
            driver: webdriver object
    """

    log = setup_logging
    globals_contents = Globals(log)
    desired_capabilities = {}
    if globals_contents.jenkins is False:
        log.info('{} - {} - {} - {} - {}'.format(
            globals_contents.target_environment,
            globals_contents.login_user_name,
            globals_contents.login_password,
            globals_contents.android_platform_version,
            globals_contents.ios_platform_version
        ))
        log.info('- Setting {} capabilities'.format(globals_contents.target_environment))

    if globals_contents.jenkins is True:
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['appPackage'] = globals_contents.AUT_PACKAGE_NAME
        desired_capabilities['appActivity'] = Globals.SPLASH_ACTIVITY_NAME
        desired_capabilities['appWaitActivity'] = Globals.NEW_LOGISTRATION_ACTIVITY_NAME

    elif globals_contents.jenkins is False and globals_contents.target_environment == strings.ANDROID:
        desired_capabilities['platformName'] = strings.ANDROID
        desired_capabilities['platformVersion'] = globals_contents.android_platform_version
        desired_capabilities['deviceName'] = globals_contents.android_device_name
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['appPackage'] = globals_contents.AUT_PACKAGE_NAME
        desired_capabilities['appActivity'] = Globals.SPLASH_ACTIVITY_NAME
        desired_capabilities['appWaitActivity'] = Globals.NEW_LOGISTRATION_ACTIVITY_NAME

    elif globals_contents.target_environment == strings.IOS:
        desired_capabilities['platformName'] = strings.IOS
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        # Required when executing on real iOS device
        # desired_capabilities['fullReset'] = True
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['bundleId'] = globals_contents.AUT_PACKAGE_NAME

    else:
        log.info('{} on - {}'.format(strings.ERROR_SETTING_CAPS, globals_contents.target_environment))
        return None

    driver = webdriver.Remote(globals_contents.server_url, desired_capabilities)

    if driver is not None:
        SharedData.driver = driver
        log.info('- Setting {} capabilities are done'.format(globals_contents.target_environment))

        def fin(request):
            request.addfinalizer(fin)

        return driver
    else:

        log.info('Problem setting {} capabilities'.format(globals_contents.target_environment))
        return None


@pytest.fixture(scope="session")
def setup_logging():
    """
    setup execution logging, it will be reusable in all files

    Returns:
            my_logger: logger object
    """

    current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%M"))

    create_result_directory(strings.RESULTS_DIRECTORY)

    iteration_directory = os.path.join(os.path.dirname(__file__), strings.RESULTS_DIRECTORY,
                                       'Iteration_{}'.format(current_day))
    create_result_directory(iteration_directory)

    logs_directory = os.path.join(iteration_directory, "logs")
    create_result_directory(logs_directory)

    screenshots_directory = os.path.join(iteration_directory, "screenshots")
    create_result_directory(screenshots_directory)
    SharedData.screenshots_directory = screenshots_directory
    log_file = os.path.join(os.path.dirname(__file__), logs_directory, strings.LOG_FILE_NAME)

    my_logger = logging.getLogger('edX Logs')
    my_logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_handler.setFormatter(formatter)
    my_logger.addHandler(log_handler)
    my_logger.info("Logging is successfully set up")
    SharedData.logger = my_logger

    def fin(request):
        request.addfinalizer(fin)
        my_logger.info("Stopping Logging")
        log_handler.close()

    return my_logger


def create_result_directory(target_directory):
    """
    Create directory by specific given name

     Argument:
            target_directory (str): directory name to create
    """

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)


# pylint: disable=redefined-outer-name
@pytest.fixture(scope="module")
def login(set_capabilities, setup_logging):
    """
    Login user based on env given, it will be reusable in tests

    Arguments:
            set_capabilities(webdriver): webdriver object
            setup_logging (logger): logger object

    Returns:
            True: if login is successful
    """

    log = setup_logging
    global_contents = Globals(log)
    is_first_time = True

    if global_contents.target_environment == strings.ANDROID:
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        assert android_new_landing_page.on_screen() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        log.info('Login screen successfully loaded')
        android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password)
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

    elif global_contents.target_environment == strings.IOS:
        ios_new_landing_page = IosNewLanding(set_capabilities, setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)

        assert ios_new_landing_page.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS
        assert ios_new_landing_page.load_login_screen().text == strings.LOGIN

        log.info('Login screen successfully loaded')
        ios_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password
        )

        is_first_time = False
        log.info('{} is successfully logged in'.format(global_contents.login_user_name))

    return is_first_time


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    """
    this function capture and add screen shot to HTML report

    :param item: default HTML report
    """

    # pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # if report.failed:
    # test_case_name = str(item)
    # file_name = test_case_name[test_case_name.find(' '):-1] + '.png'
    # file_path = SharedData.screenshots_directory + '/' + file_name
    # SharedData.driver.save_screenshot(file_path)
    # html = '<div><img src="{}" alt="screenshot" style="width:304px;height:228px;" ' \
    #     'onclick="window.open(this.src)" align="right"/></div>'.format(file_path)
    # extra.append(pytest_html.extras.html(html))
    report.extra = extra


class SharedData:
    """class to access necessary shared info"""

    driver: webdriver.Remote = None
    screenshots_directory = None
    logger = None
