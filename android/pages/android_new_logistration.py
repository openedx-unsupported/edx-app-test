"""
    New Logistrtion Page Module
"""

from time import sleep

from android.pages.android_base_page import AndroidBasePage
from common.globals import Globals
from common import strings
from android.pages import android_elements

class AndroidNewLogistration(AndroidBasePage):
    """
    New Logistration screen
    """

    def load_app(self):
        """
        Load New Logistration screen

        Returns:
            str: New Logistration Activity Name
        """

        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def get_edx_logo(self):
        """
        Get edX logo

        Returns:
            webdriver element: Logo element
        """

        image_edx_logo = self.driver.find_element_by_id(android_elements.new_logistration_logo)
        return self.global_contents.validate_element(
            image_edx_logo,
            image_edx_logo.text,
            strings.BLANK_FIELD,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_discover_course_button(self):
        """
        Get Discover Button

        Returns:
            webdriver element: Discover Button element
        """

        button_discover_courses = self.driver.find_element_by_id(
            android_elements.new_logistration_discover_courses_button
            )

        return self.global_contents.validate_element(
            button_discover_courses,
            button_discover_courses.text,
            strings.NEW_LOGIS_DISCOVER_COURSES,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_register_button(self):
        """
        Get Register Button

        Returns:
            webdriver element: Register Button element
        """

        button_register = self.driver.find_element_by_id(android_elements.new_logistration_register_button)

        return self.global_contents.validate_element(
            button_register, button_register.text,
            strings.NEW_LOGIS_REGISTER,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_signin_button(self):
        """
        Get Login Button

        Returns:
            webdriver element: Login Button element
        """

        button_login = self.driver.find_element_by_id(android_elements.new_logistration_sign_in_button)
        return self.global_contents.validate_element(
            button_login, button_login.text,
            strings.NEW_LOGIS_LOGIN,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def load_login_screen(self):
        """
        Load Login Screen

        Returns:
             str: Login Activity Name
        """

        self.get_signin_button().click()
        sleep(self.global_contents.medium_timeout)
        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def load_register_screen(self):
        """
        Load Register Screen

        Returns:
             str: Register Activity Name
        """

        self.get_register_button().click()
        sleep(self.global_contents.medium_timeout)
        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def load_discover_courses_screen(self):
        """
        Load Discover Courses Screen

        Returns:
             str: Discover Courses Activity Name
        """

        self.get_discover_course_button().click()
        sleep(self.global_contents.medium_timeout)
        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def back_and_forth_login(self):

        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Login screen
        """

        if self.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME:
            self.driver.back()
            sleep(self.global_contents.minimum_timeout)
            return self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        else:
            self.log.info('Problem - Login screen is not loaded')
            return False

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Register screen
        """

        if self.load_register_screen() == Globals.REGISTER_ACTIVITY_NAME:
            self.driver.back()
            sleep(self.global_contents.minimum_timeout)
            return self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        else:
            self.log.info('Problem - Register screen is not loaded')
            return False

    def back_and_forth_dicover_courses(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Discover Courses screen
        """

        if self.load_discover_courses_screen() == Globals.DISCOVERY_ACTIVITY_NAME:
            self.driver.back()
            sleep(self.global_contents.minimum_timeout)
            return self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        else:
            self.log.info('Problem - Discovery screen is not loaded')
            return False
