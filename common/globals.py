"""
   Module covers Android & iOS screens' global contents
"""
from time import sleep
import sys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common import strings

class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """

    # Android Activities Names
    AUT_PACKAGE_NAME = 'org.edx.mobile'
    SERVER_URL = 'http://localhost:4723/wd/hub'
    LAUNCH_ACTIVITY_NAME1 = '.view.LaunchActivity'
    SPLASH_ACTIVITY_NAME = '.view.SplashActivity'
    NEW_LOGISTRATION_ACTIVITY_NAME = '.view.DiscoveryLaunchActivity'
    LOGIN_ACTIVITY_NAME = '.view.LoginActivity'
    TERMS_AND_CONDITIONS_ACTIVITY_NAME = '.view.dialog.WebViewActivity'
    WHATS_NEW_ACTIVITY_NAME = '.whatsnew.WhatsNewActivity'
    VIEW_MY_COURSES_ACTIVITY_NAME = '.view.MyCoursesListActivity'
    REGISTER_ACTIVITY_NAME = '.view.RegisterActivity'
    DISCOVERY_ACTIVITY_NAME = '.view.WebViewFindCoursesActivity'

    def __init__(self, project_log):
        self.medium_timeout = 5
        self.maximum_timeout = 8
        self.minimum_timeout = 2
        self.flag = True
        self.is_first_time = False

        # CAPABILITIES
        self.ios_platform_version = '11.2'
        self.ios_device_name = 'iPhone Simulator'
        self.android_platform_version = '8.0'
        self.android_device_name = 'Nexus 6P'
        self.project_log = project_log

    def wait_and_get_element(self, driver, element_locator):
        """
        Block until the element present on screen, then returns the element

        Arguments:
            arg1 (webdriver element) : target_element
            arg2 (str) : element_value
            arg3 (str) : expected_value
            arg4 (str) : error_msg

        Return:
            webdriver element: target_element
        """

        try:
            self.element = WebDriverWait(driver, self.maximum_timeout).until(
                expected_conditions.presence_of_element_located((By.ID, element_locator)))

            self.project_log.info('Found - {} - {} - {}'.format(
                self.element,
                self.element.tag_name,
                self.element.text
            ))
            return self.element

        except ElementNotInteractableException as element_not_interactable_exception:
            self.project_log.debug('ElementNotInteractableException caught {}'.format(
                element_not_interactable_exception
            ))

        except Exception as any_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                element_locator,
                any_exception,
                sys.exc_info()[0]
            ))

    def get_all_views_on_screen(self, driver, target_elements):
        """
        Get list of Views on screen

        Argument:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        try:
            all_views = WebDriverWait(driver, self.maximum_timeout).until(
                expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target_elements)))
            if all_views:
                if len(all_views) > 0:
                    self.project_log.error('Total {} - {} found on screen'.format(len(all_views), target_elements))
                    return all_views
                else:
                    self.project_log.error('0 {} found on screen'.format(target_elements))
            else:
                return None

        except ElementNotInteractableException as element_not_interactable_exception:
            self.project_log.debug('ElementNotInteractableException caught {}'.format(
                element_not_interactable_exception
            ))

        except Exception as any_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                any_exception,
                sys.exc_info()[0]
            ))

    def wait_for_element_visblility(self, driver, target_elements):
        """
            Block until the element visibility on screen, then returns True

            Keyword Args:
                driver (webdriver element): webdriver instance variable
                target_elements (str): specific selector of element

            Raises:
                TimeOut: The timeout is exceeded without the element successfully visible
            """
        try:
            self.out_put = WebDriverWait(driver, self.medium_timeout).until(
                expected_conditions.visibility_of_element_located((
                    By.ID,
                    target_elements
                )))
            return True

        except Exception as any_exception:
            self.project_log.error('{} - {} - {} '.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                any_exception,
                sys.exc_info()[0]
            ))
            return False

    def wait_for_element_invisblility(self, driver, target_elements):
        """
            Block until the element invisibility on screen, then returns True

            Keyword Args:
                driver (webdriver element): webdriver instance variable
                target_elements (str): specific selector of element
            """
        try:
            self.out_put = WebDriverWait(driver, self.medium_timeout).until(
                expected_conditions.invisibility_of_element_located((
                    By.ID,
                    target_elements
                )))
            return True

        except Exception as any_exception:
            self.project_log.error('{} - {} - {} '.format(
                strings.ERROR_UTF_ELEMENT,
                target_elements,
                any_exception,
                sys.exc_info()[0]
            ))
            return False

    def scroll_screen(self, driver, from_element, to_element):
        """
        Scroll from one element to other element on screen

        Arguments:
            driver (webdriver element): webdriver instance variable
            from_element (webdriver element): element from wthich scroll will start
            to_element (webdriver element): element where scroll will end
        """
        self.project_log.info('Scrolling screen.')
        driver.scroll(from_element, to_element)
