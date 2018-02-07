"""
    New Logistrtion Page Module
"""

from time import sleep
from common import strings
from ios.pages.ios_base_page import IosBasePage
from ios.pages import ios_elements


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

        button_discover_courses = self.driver.find_element_by_id(
            ios_elements.new_logistration_discover_courses_button
        )

        return button_discover_courses

    def get_edx_logo(self):
        """
        Get edX logo

        Returns:
            webdriver element: Logo element
        """

        all_images = self.driver.find_elements_by_class_name(ios_elements.new_logistration_logo)
        image_edx_logo = all_images[1]
        return image_edx_logo

    def get_discover_course_button(self):
        """
        Get Discover Button

        Returns:
            webdriver element: Discover Button element
        """

        button_discover_courses = self.driver.find_element_by_id(
            ios_elements.new_logistration_discover_courses_button
            )
        return button_discover_courses

    def get_register_button(self):
        """
        Get Register Button

        Returns:
            webdriver element: Register Button element
        """

        button_register = self.driver.find_element_by_id(ios_elements.new_logistration_register_button)
        return button_register

    def get_signin_button(self):
        """
        Get Login Button

        Returns:
            webdriver element: Login Button element
        """

        button_login = self.driver.find_element_by_id(ios_elements.new_logistration_sign_in_button)
        return button_login

    def load_login_screen(self):
        """
        Load Login Screen

        Returns:
             str: Login screen Title element
        """

        self.get_signin_button().click()
        sleep(self.global_contents.medium_timeout)
        textview_screen_title = self.driver.find_element_by_id(ios_elements.login_title_textview)
        return textview_screen_title

    def load_register_screen(self):
        """
        Load Register Screen

        Returns:
             str: Register screen Title element
        """

        self.get_register_button().click()
        sleep(self.global_contents.medium_timeout)
        textview_screen_title = self.driver.find_element_by_id(ios_elements.register_title_textview)
        return textview_screen_title

    def load_discover_courses_screen(self):
        """
        Load Discover Courses Screen

        Returns:
             str: Discover Courses screen Title element
        """

        self.get_discover_course_button().click()
        sleep(self.global_contents.medium_timeout)
        textview_screen_title = self.driver.find_element_by_id(ios_elements.discover_courses_title_textview)
        return textview_screen_title

    def back_and_forth_login(self):

        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Login screen
        """

        if self.load_login_screen().text == strings.LOGIN_SCREEN_TITLE:
            all_buttons = self.driver.find_elements_by_class_name(ios_elements.all_buttons)

            all_buttons[0].click()
            sleep(self.global_contents.minimum_timeout)
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
            all_buttons = self.driver.find_elements_by_class_name(ios_elements.all_buttons)
            all_buttons[0].click()
            sleep(self.global_contents.minimum_timeout)
            return self.get_discover_course_button().text == strings.NEW_LOGIS_DISCOVER_COURSES

        else:
            self.log.info('Problem - Register screen is not loaded')
            return False

    def back_and_forth_dicover_courses(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Discover Courses screen
        """

        if self.load_discover_courses_screen().text == strings.DISCOVER_COURSES_SCREEN_TITLE:
            all_buttons = self.driver.find_elements_by_class_name(ios_elements.all_buttons)
            all_buttons[0].click()
            sleep(self.global_contents.minimum_timeout)
            return self.get_discover_course_button().text == strings.NEW_LOGIS_DISCOVER_COURSES
        else:
            self.log.info('Problem - Discovery screen is not loaded')
            return False
