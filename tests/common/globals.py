# coding=utf-8
"""
   Module covers Android & iOS screens' global contents
"""

import sys
import string
import random
import yaml

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.common import strings


class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """

    # Register
    AUT_PACKAGE_NAME = 'org.edx.mobile'
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
    WEB_VIEW_FIND_COURSES_ACTIVITY_NAME = '.view.WebViewFindCoursesActivity'
    WITHOUT_LOGIN_DISCOVERY_ACTIVITY_NAME = '.view.DiscoveryActivity'
    DISCOVERY_LAUNCH_ACTIVITY_NAME = '.view.DiscoveryLaunchActivity'
    EULA_ACTIVITY_NAME = '.view.dialog.WebViewActivity'
    PROFILE_ACTIVITY_NAME = '.profiles.UserProfileActivity'
    ACCOUNT_ACTIVITY_NAME = '.view.AccountActivity'
    COURSE_DASHBOARD_ACTIVITY_NAME = '.view.CourseTabsDashboardActivity'
    LANDSCAPE_ORIENTATION = 'LANDSCAPE'
    PORTRAIT_ORIENTATION = 'PORTRAIT'

    def __init__(self, project_log):
        self.medium_timeout = 5
        self.maximum_timeout = 15
        self.minimum_timeout = 2
        self.index = 0
        self.flag = True
        self.is_first_time = True
        self.android_search_key = 84
        self.android_enter_key = 66
        self.first_existence = 0
        self.second_existence = 1
        self.third_existence = 2
        self.fourth_existence = 3
        self.fifth_existence = 4
        self.sixth_existence = 5
        self.seventh_existence = 6
        self.eight_existence = 7
        self.ninth_existence = 8
        self.tenth_existence = 9
        self.eleventh_existence = 10
        self.twelfth_existence = 11
        self.thirteenth_existence = 12
        self.fourteenth_existence = 13
        self.fifteenth_existence = 14
        self.sixteenth_existence = 15

        # Read  user_preferences.yml and set globals accordingly
        with open("user_preferences.yml") as user_file:
            user_preferences = yaml.safe_load(user_file)
            user_file.close()

        # CAPABILITIES
        self.ios_device_name = 'iPhone Simulator'
        self.android_device_name = 'Android Phone'
        self.server_url = user_preferences.get('Settings').get('appium_server')
        self.target_environment = user_preferences.get('Settings').get('target_environment')
        self.android_platform_version = user_preferences.get('Settings').get('android_platform_version')
        self.ios_platform_version = user_preferences.get('Settings').get('ios_platform_version')
        self.login_user_name = user_preferences.get('User').get('login_user_name')
        self.login_password = user_preferences.get('User').get('login_password')

        self.login_wrong_user_name = 'wrong username'
        self.login_wrong_password = 'wrong password'
        self.new_landing_search_courses = 'python'
        self.country = 'Argentina'
        self.project_log = project_log
        self.screen_width = ''
        self.screen_height = ''
        self.element_x_position = ''
        self.element_y_position = ''
        self.element_width = ''
        self.element_height = ''

    def wait_and_get_element(self, driver, element_locator, optional_time=None):
        """
        Block until the element present on screen, then returns the element

        Arguments:
            driver (webdriver): webdriver instance variable
            element_locator (webdriver element) : target elements locator

        Return:
            webdriver element: target_element
        """
        element = None
        time_out = self.maximum_timeout

        if optional_time is not None:
            time_out = optional_time

        try:
            if self.target_environment == strings.ANDROID:
                element = WebDriverWait(driver, time_out).until(
                    expected_conditions.presence_of_element_located((By.ID, element_locator)))
            elif self.target_environment == strings.IOS:
                element = WebDriverWait(driver, time_out).until(
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
            if self.target_environment == strings.ANDROID:
                all_views = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target_elements)))
            elif self.target_environment == strings.IOS:
                all_views = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_all_elements_located((MobileBy.ACCESSIBILITY_ID, target_elements)))
            self.index = 0
            if all_views:
                no_of_all_views = len(all_views)
                if no_of_all_views > 0:
                    self.project_log.info('Total {} - {} found on screen'.format(len(all_views), target_elements))
                    for view in all_views:
                        self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                        self.index += 1
                    return all_views
                else:
                    self.project_log.info('0 {} found on screen'.format(target_elements))

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

    def get_all_views_on_ios_screen(self, driver, target_elements):
        """
        Get list of all visible Views on ios screen

        Arguments:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        try:
            all_views = WebDriverWait(driver, self.maximum_timeout).until(
                expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target_elements)))
            self.index = 0
            if all_views:
                no_of_all_views = len(all_views)
                if no_of_all_views > 0:
                    self.project_log.info('Total {} - {} found on screen'.format(len(all_views), target_elements))
                    for view in all_views:
                        self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                        self.index += 1

                    return all_views
                else:
                    self.project_log.info('0 {} found on screen'.format(target_elements))

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

    def get_all_views_on_screen_by_id(self, driver, target_elements):
        """
        Get list of Views on screen

        Arguments:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        try:
            all_views = WebDriverWait(driver, self.medium_timeout).until(
                expected_conditions.presence_of_all_elements_located((By.ID, target_elements)))
            if all_views:
                self.project_log.info('Total {} - {} found on screen'.format(len(all_views), target_elements))
                for view in all_views:
                    self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                    self.index += 1
                return all_views
            else:
                self.project_log.error('0 {} found on screen'.format(target_elements))
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

    def get_elements_from_list(self, driver, target_list, target_elements):
        """
        Get elements from given list

        Arguments:
            driver (webdriver): webdriver instance variable
            target_list (str): list locator
            target_elements (str): elements locator

        Return:
            webdriver elements: List of elements into specific list
        """

        try:
            parent_element = WebDriverWait(driver, self.medium_timeout).until(
                expected_conditions.presence_of_element_located((By.ID, target_list)))

            elements = parent_element.find_elements_by_id(target_elements)

            if elements:
                self.project_log.info('Total {} - {} found in List'.format(len(elements), target_elements))
                for view in elements:
                    self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                    self.index += 1

                return elements
            else:
                self.project_log.error('0 {} found in List'.format(target_elements))
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
        element = None

        try:
            if self.target_environment == strings.ANDROID:
                element = WebDriverWait(driver, self.medium_timeout).until(
                    expected_conditions.visibility_of_element_located((
                        By.ID,
                        target_elements
                    )))
            elif self.target_environment == strings.IOS:
                element = WebDriverWait(driver, self.medium_timeout).until(
                    expected_conditions.visibility_of_element_located((
                        MobileBy.ACCESSIBILITY_ID,
                        target_elements
                    )))

            return element

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

    def scroll_from_element(self, driver, from_element):
        """
        Scroll from element

        Arguments:
            driver (webdriver element): webdriver instance variable
            from_element (webdriver element): element from which scroll will start
        """

        screen_width = driver.get_window_size()["width"]
        screen_height = driver.get_window_size()["height"]
        element_x_position = from_element.location['x']
        element_y_position = from_element.location['y']

        self.project_log.info('screen width {} - screen height {} - element_x {} - ''element_y {} '.format(
            screen_width,
            screen_height,
            element_x_position,
            element_y_position
            ))

        horizontal_start_point = int(element_x_position)
        vertical_start_point = int(element_y_position)
        horizontal_end_point = int(element_x_position)
        vertical_end_point = 0

        self.project_log.info('horizontal_start_point {} - vertical_start_point {} - horizontal_end_point {} '
                              '- vertical_end_point {} '.format(horizontal_start_point,
                                                                vertical_start_point,
                                                                horizontal_end_point,
                                                                vertical_end_point
                                                                ))

        driver.swipe(horizontal_start_point, vertical_start_point, horizontal_end_point, vertical_end_point, 500)

    def swipe_screen(self, driver):
        """
        Scroll/swipe from bottom to top end of screen

        Arguments:
            driver (webdriver element): webdriver instance variable
        """

        screen_width = driver.get_window_size()["width"]
        screen_height = driver.get_window_size()["height"]

        horizontal_start_point = int((screen_width * 40) / 100)
        vertical_start_point = int((screen_height * 95) / 100)
        horizontal_end_point = horizontal_start_point
        vertical_end_point = int((screen_width * 5) / 100)

        self.project_log.info('Screen width {} -screen height {} - horizontal_start_point {} '
                              '- vertical_start_point {} '
                              '- horizontal_end_point {} '
                              '- vertical_end_point {}'.format(screen_width, screen_height,
                                                               horizontal_start_point, vertical_start_point,
                                                               horizontal_end_point, vertical_end_point
                                                               ))
        driver.swipe(horizontal_start_point, vertical_start_point, horizontal_end_point, vertical_end_point, 500)

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
                target_activity,
                strings.ERROR_SCREEN_NOT_LOADED,
                driver.current_activity,
                web_driver_exception,
                sys.exc_info()[0]
            ))

            return False

    def get_element_coordinates(self, driver, target_element):
        """
        Get height, width, and coordinates of specific given element

        Arguments:
            driver (webdriver element): webdriver instance variable
            target_element (str): specific element

        """

        element = self.wait_and_get_element(
            driver,
            target_element
        )
        self.screen_width = driver.get_window_size()["width"]
        self.screen_height = driver.get_window_size()["height"]

        self.element_x_position = element.location['x']
        self.element_y_position = element.location['y']
        self.element_width = element.rect['width']
        self.element_height = element.rect['height']

        self.project_log.info('Screen width{}-screen height{} -element_x{} -element_y{} -element_width{} '
                              '-element_height{}'.format(self.screen_width, self.screen_height,
                                                         self.element_x_position, self.element_y_position,
                                                         self.element_width, self.element_height
                                                         ))

    def turn_orientation(self, driver, target_orientation):
        """
        Change device orientation

        Arguments:
            driver (webdriver element): webdriver instance variable
            target_orientation (str): target orientation to change
        """

        if driver.orientation == target_orientation:
            self.project_log.info('{} is already set '.format(target_orientation))
        else:
            self.project_log.info('Turning orientation to {}'.format(target_orientation))
            driver.orientation = target_orientation

    def generate_random_credentials(self, length):
        """
        Generate random alphanumeric strings

        Arguments:
            length (int): length of string to generate

        Return:
            str: random string
        """

        combination = string.ascii_lowercase + string.digits
        return ''.join(random.choice(combination) for _ in range(length))

    def tap_on_element(self, driver, target_element):

        """
        Tap on element's coordinates

        Arguments:
           driver (webdriver element): webdriver instance variable
           target_element (str): specific element

        """

        self.element_x_position = target_element.location['x']
        self.element_y_position = target_element.location['y']
        self.element_width = target_element.rect['width']
        self.element_height = target_element.rect['height']

        self.project_log.info('element_x {} - element_y {} - element_width {} '
                              '- element_height {}'.format(self.element_x_position, self.element_y_position,
                                                           self.element_width, self.element_height
                                                           ))

        horizontal_start_point = int(self.element_x_position)
        vertical_start_point = int(self.element_y_position)
        horizontal_end_point = int(self.element_x_position + (self.element_x_position * 10)/100)
        vertical_end_point = int(self.element_y_position + (self.element_y_position * 10)/100)

        coordinates = [(horizontal_start_point, vertical_start_point), (horizontal_end_point, vertical_end_point)]
        self.project_log.info('Tapping on element_x {} - element_y {} - element_width {} '
                              '- element_height {}'.format(horizontal_start_point, vertical_start_point,
                                                           horizontal_end_point, vertical_end_point
                                                           ))
        driver.tap(coordinates)


class WaitForActivity:
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
            self.log.info('On {} '.format(self.target_activity))
            return self.driver.current_activity

        else:
            self.log.error('{} - {} '.format(self.target_activity, strings.ERROR_SCREEN_NOT_LOADED))
            return False
