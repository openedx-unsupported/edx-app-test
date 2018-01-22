"""
   Module covers Android & iOS screens' global contents
"""
from time import sleep
from common import strings


class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """
    # Android Activities Names
    AUT_PACKAGE_NAME = 'org.edx.mobile'
    LAUNCH_ACTIVITY_NAME1 = '.view.LaunchActivity'
    SPLASH_ACTIVITY_NAME = '.view.SplashActivity'
    NEW_LOGISTRATION_ACTIVITY_NAME = '.view.DiscoveryLaunchActivity'
    LOGIN_ACTIVITY_NAME = '.view.LoginActivity'
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
        self.SERVER_URL = 'http://localhost:4723/wd/hub'
        self.APP_PACKAGE_NAME = 'org.edx.mobile'
        self.ios_device_name = 'iPhone Simulator'
        self.ios_platform_version = '10.3'
        self.android_device_name = 'Nexus 6P'
        self.android_platform_version = '8.0'
        self.project_log = project_log

    def validate_element(self, target_element, element_value, expected_value, error_msg):
        """
        Get element on screen and validate its visible value/label

        Arguments:
            arg1 (webdriver element) : target_element
            arg2 (str) : element_value
            arg3 (str) : expected_value
            arg4 (str) : error_msg

        Return:
            webdriver element: target_element
        """

        optimise_error = error_msg, 'Target - {} - expected - {}'.format(element_value, expected_value)
        if target_element is not None:
            if element_value == expected_value:
                self.project_log.info('Found - {} - {} - {} - {}'.format(
                    target_element,
                    target_element.tag_name,
                    element_value,
                    expected_value
                    ))
                return target_element
            else:
                self.project_log.error('{} - {} - {} - {} - {}'.format(
                    strings.ERROR_LABEL_NOT_MATCHING,
                    target_element,
                    target_element.tag_name,
                    element_value,
                    expected_value
                    ))

                return None, False
        else:
            self.project_log.error('{} - {} - {} - {}'.format(
                strings.ERROR_UTF_ELEMENT,
                optimise_error,
                target_element,
                target_element.tag_name
            ))
            return None, False

    def get_all_views(self, driver, target_elements):
        """
        Get list of all Views on screen

        Argument:
            arg1 (webdriver) : driver
            arg2 (webdriver element) : target_elements

        Return:
            webdriver element: List of Views
        """

        all_views = driver.find_elements_by_class_name(target_elements)

        if all_views is not None:
            if len(all_views) > 0:
                self.project_log.info('Total {} Views found on screen'.format(len(all_views)))
            return all_views

        else:
            self.project_log.info('0 {} Views on screen'.format(target_elements))
            return None, False

    def scroll_screen(self, driver, from_element, to_element):
        """
        Scroll from one element to other element on screen

        Arguments:
            arg1 (webdriver element) : from_element
            arg2 (webdriver element) : to_element
        """

        sleep(self.minimum_timeout)
        self.project_log.info('Scrolling screen.')
        driver.scroll(from_element, to_element)
        sleep(self.minimum_timeout)
