"""
    New Landing Page Module
"""
from selenium.webdriver.common.keys import Keys

from common import strings
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


class IosNewLanding(IosBasePage):
    """
    New Landing screen
    """

    def get_edx_logo(self):
        """
        Get edX logo

        Returns:
            webdriver element: Logo element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_landing_logo
        )

    def get_welcome_message(self):
        """
        Get welcome message text

        Returns:
            webdriver element: Welcome Message element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_landing_welcome_message
        )

    def get_search_course_editfield(self):
        """
        Get Search Courses edit field

        Returns:
            webdriver element: Search Courses element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_landing_search_courses_editfield
        )

    def get_register_button(self):
        """
        Get Register Button

        Returns:
            webdriver element: Register Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_landing_register_button
        )

    def get_signin_button(self):
        """
        Get Login Button

        Returns:
            webdriver element: Login Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.new_landing_log_in_button
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

    def search_courses(self, course_name):
        """
        Search some Course and load Discovery Screen

        Arguments:
            course_name (str): course name

        Returns:
            webdriver element: Cancel Element
        """

        search_courses = self.get_search_course_editfield()
        search_courses.clear()
        search_courses.send_keys(course_name)
        search_courses.send_keys(Keys.ENTER)
        self.discovery_cancel_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.discovery_close_button
        )

        return self.discovery_cancel_button

    def cancel_discovery_screen(self):
        """
        Close/Cancel Discovery Screen
        """

        self.discovery_cancel_button.click()

    def back_and_forth_login(self):
        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Landing screen from Login screen
        """

        if self.load_login_screen().text == strings.LOGIN:
            login_close_button = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.login_close_button
            )
            login_close_button.click()

            return self.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS

        else:
            self.log.info('Problem - Login screen is not loaded')
            return False

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Landing screen from Register screen
        """

        if self.load_register_screen().text == strings.REGISTER_SCREEN_REGISTER_WITH:
            register_close_button = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.register_close_button
            )
            register_close_button.click()

            return self.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS

        else:
            self.log.info('Problem - Register screen is not loaded')
            return False
