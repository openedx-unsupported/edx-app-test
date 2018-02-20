"""
    New Logistration Page Module
"""

from common import strings
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


class IosNewLogistration(IosBasePage):
    """
    New Logistration screen
    """

    def load_app(self):
        """
        Load New Logistration screen

        Returns:
            webdriver element: Discover Course button element
        """

        return self.get_discover_course_button()

    def get_edx_logo(self):
        """
        Get edX logo

        Returns:
            webdriver element: Logo element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_logistration_logo
        )

    def get_discover_course_button(self):
        """
        Get Discover Button

        Returns:
            webdriver element: Discover Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_logistration_discover_courses_button
        )

    def get_register_button(self):
        """
        Get Register Button

        Returns:
            webdriver element: Register Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_logistration_register_button
        )

    def get_signin_button(self):
        """
        Get Login Button

        Returns:
            webdriver element: Login Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_logistration_sign_in_button
        )

    def load_login_screen(self):
        """
        Load Login Screen

        Returns:
             webdriver element: Login screen Title element
        """

        self.get_signin_button().click()
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_signin_button
        )

    def load_register_screen(self):
        """
        Load Register Screen

        Returns:
             webdriver element: Register screen Title element
        """

        self.get_register_button().click()
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_with_textview
        )

    def load_discover_courses_screen(self):
        """
        Load Discover Courses Screen

        Returns:
             webdriver element: Discover Courses screen Title element
        """

        self.get_discover_course_button().click()

        self.discovery_close_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.discovery_close_button
        )

        return self.discovery_close_button

    def back_and_forth_login(self):

        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Login screen
        """

        if self.load_login_screen().text == strings.LOGIN:
            login_close_button = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.login_close_button
            )
            login_close_button.click()

            return self.get_discover_course_button().text == strings.NEW_LOGIS_DISCOVER_COURSES
        else:
            self.log.info('Problem - Login screen is not loaded')
            return False

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Register screen
        """

        if self.load_register_screen().text == strings.REGISTER_SCREEN_TITLE:
            register_close_button = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.register_close_button
            )
            register_close_button.click()

            return self.get_discover_course_button().text == strings.NEW_LOGIS_DISCOVER_COURSES

        else:
            self.log.info('Problem - Register screen is not loaded')
            return False

    def back_and_forth_discover_courses(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Discover Courses screen
        """

        if self.load_discover_courses_screen().text == strings.DISCOVER_CANCEL:
            self.discovery_close_button.click()
            return self.get_discover_course_button().text == strings.NEW_LOGIS_DISCOVER_COURSES
        else:
            self.log.info('Problem - Discovery screen is not loaded')
            return False
