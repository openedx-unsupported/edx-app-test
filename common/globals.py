"""
   Module covers Android & iOS screens' global contents
"""

import sys
from os import environ

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common import strings


class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """

    AUT_PACKAGE_NAME = 'org.edx.mobile'
    SERVER_URL = 'http://localhost:4723/wd/hub'
    # Android Activities Names
    LAUNCH_ACTIVITY_NAME1 = '.view.LaunchActivity'
    SPLASH_ACTIVITY_NAME = '.view.SplashActivity'
    NEW_LOGISTRATION_ACTIVITY_NAME = '.view.DiscoveryLaunchActivity'
    LOGIN_ACTIVITY_NAME = '.view.LoginActivity'
    TERMS_AND_CONDITIONS_ACTIVITY_NAME = '.view.dialog.WebViewActivity'
    WHATS_NEW_ACTIVITY_NAME = '.whatsnew.WhatsNewActivity'
    VIEW_MY_COURSES_ACTIVITY_NAME = '.view.MyCoursesListActivity'
    MAIN_DASHBOARD_ACTIVITY_NAME = '.view.MainDashboardActivity'
    REGISTER_ACTIVITY_NAME = '.view.RegisterActivity'
    DISCOVERY_ACTIVITY_NAME = '.view.WebViewFindCoursesActivity'

    def __init__(self, project_log):
        self.medium_timeout = 5
        self.maximum_timeout = 8
        self.minimum_timeout = 2
        self.flag = True
        self.is_first_time = False

        self.target_environment = environ.get('TARGET_ENVIRONMENT')
        self.login_user_name = environ.get('LOGIN_USER_NAME')
        self.login_password = environ.get('LOGIN_PASSWORD')

        # CAPABILITIES
        self.ios_platform_version = environ.get('IOS_PLATFORM_VERSION')
        self.ios_device_name = 'iPhone Simulator'
        self.android_platform_version = environ.get('ANDROID_PLATFORM_VERSION')
        self.android_device_name = 'Android Phone'
        self.project_log = project_log

    def wait_and_get_element(self, driver, element_locator):
        """
        Block until the element present on screen, then returns the element

        Arguments:
            driver (webdriver): webdriver instance variable
            element_locator (webdriver element) : target elements locator

        Return:
            webdriver element: target_element
        """
        element = None

        try:
            if self.target_environment == strings.ANDROID:
                element = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_element_located((By.ID, element_locator)))
            elif self.target_environment == strings.IOS:
                element = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, element_locator)))

            self.project_log.info('Found - {} - {} - {} - {}'.format(
                element_locator,
                element.tag_name,
                element.text,
                element
            ))
            return element

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                element_locator,
                no_such_element_exception,
                sys.exc_info()[0]))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                element_locator,
                web_driver_exception,
                sys.exc_info()[0]))

    def get_all_views_on_screen(self, driver, target_elements):
        """
        Get list of Views on screen

        Arguments:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        all_views = None

        try:
            if self.target_environment.target_environment == strings.ANDROID:
                all_views = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target_elements)))
            elif self.target_environment.target_environment == strings.IOS:
                all_views = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_all_elements_located((MobileBy.ACCESSIBILITY_ID, target_elements)))

            if all_views:
                if len(all_views) > 0:
                    self.project_log.error('Total {} - {} found on screen'.format(len(all_views), target_elements))
                    return all_views
                else:
                    self.project_log.error('0 {} found on screen'.format(target_elements))
            else:
                return None

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))

    def wait_for_element_visibility(self, driver, target_elements):
        """
        Block until the element visibility on screen, then returns True

        Arguments:
            driver (webdriver element): webdriver instance variable
            target_elements (str): specific selector of element

        Raises:
            TimeOut: The timeout is exceeded without the element successfully visible
        """

        try:

            return WebDriverWait(driver, self.medium_timeout).until(
                expected_conditions.visibility_of_element_located((
                    By.ID,
                    target_elements
                )))

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {} '.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {} '.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))

            return False

    def wait_for_element_invisibility(self, driver, target_elements):
        """
        Block until the element invisibility on screen, then returns True

        Arguments:
            driver (webdriver element): webdriver instance variable
            target_elements (str): specific selector of element
        """

        try:
            return WebDriverWait(driver, self.medium_timeout).until(
                expected_conditions.invisibility_of_element_located((
                    By.ID,
                    target_elements
                )))

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {} '.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))
            return False

    def scroll_screen(self, driver, from_element, to_element):
        """
        Scroll from one element to other element on screen

        Arguments:
            driver (webdriver element): webdriver instance variable
            from_element (webdriver element): element from which scroll will start
            to_element (webdriver element): element where scroll will end
        """

        self.project_log.info('Scrolling screen.')
        driver.scroll(from_element, to_element)

    def wait_for_android_activity_to_load(self, driver, target_activity):
        """
        Block until specific Android screen is loaded, then returns True

        Arguments:
            driver (webdriver element): webdriver instance variable
            target_activity (str): specific activity to wait for
        """

        try:
            return WebDriverWait(driver, self.medium_timeout).until(
                WaitForActivity(
                    target_activity,
                    self.project_log
                ), driver)

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {} - {}'.format(
                strings.ERROR_SCREEN_NOT_LOADED,
                driver.current_activity,
                target_activity,
                web_driver_exception,
                sys.exc_info()[0]
            ))

            return False


class WaitForActivity(object):
    """
    An expectation for checking specific activity is loaded
    """

    def __init__(self, target_activity, logs):
        self.target_activity = target_activity
        self.log = logs
        self.driver = None

    def __call__(self, driver):
        """
        Arguments:
                driver (webdriver): webdriver instance variable

        Return:
            activity: visible activity name

        """
        self.driver = driver
        if self.driver.current_activity == self.target_activity:
            self.log.info('on {} '.format(self.target_activity))
            return self.driver.current_activity

        else:
            self.log.error('{} - {} '.format(self.target_activity, strings.ERROR_SCREEN_NOT_LOADED))
            return False
