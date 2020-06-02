# coding=utf-8
"""
    New Landing Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidNewLanding(AndroidBasePage):
    """
    New Landing screen
    """

    def on_screen(self):
        """
        Load New Landing screen

        Returns:
            str: New Landing screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        )

    def get_edx_logo(self):
        """
        Get edX logo
        Returns:
            webdriver element: Logo element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_landing_logo
        )

    def get_welcome_message(self):
        """
        Get welcome message text

        Returns:
            webdriver element: Welcome Message element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_landing_welcome_message
        )

    def get_search_course_icon(self):
        """
        Get Search Courses icon

        Returns:
            webdriver element: Search Courses icon element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_landing_search_courses_editfield
        )

    def get_search_course_editfield(self):
        """
        Get Search Courses edit field

        Returns:
            webdriver element: Search Courses editfield element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_landing_search_courses_editfield
        )

    def get_register_button(self):
        """
        Get Register Button

        Returns:
            webdriver element: Register Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_landing_register_button
        )

    def get_signin_button(self):
        """
        Get Login Button

        Returns:
            webdriver element: Login Button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.new_landing_log_in_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_landing_log_in_button
        )

    def load_login_screen(self):
        """
        Load Login Screen

        Returns:
             str: Login Activity Name
        """

        self.get_signin_button().click()
        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.LOGIN_ACTIVITY_NAME
        )

    def load_register_screen(self):
        """
        Load Register Screen

        Returns:
             str: Register Activity Name
        """

        self.get_register_button().click()
        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.REGISTER_ACTIVITY_NAME
        )

    def search_courses(self, course_name):
        """
        Search some Course and load Discovery Screen

        Arguments:
            course_name (str): course name

        Returns:
            str: Find Courses Activity Name
        """

        search_courses = self.get_search_course_editfield()
        search_courses.clear()
        search_courses.click()
        search_courses.send_keys(course_name)
        self.driver.press_keycode(self.global_contents.android_enter_key)

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.WITHOUT_LOGIN_DISCOVERY_ACTIVITY_NAME
        )

    def back_and_forth_login(self):
        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Landing screen from Login screen
        """

        self.global_contents.flag = False
        if self.driver.current_activity == self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME:
            if self.load_login_screen() == self.global_contents.LOGIN_ACTIVITY_NAME:
                self.driver.back()
                if self.global_contents.wait_for_android_activity_to_load(
                    self.driver,
                    self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
                ) == self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME:
                    self.global_contents.flag = True
                else:
                    self.log.error('New Landing screen is not loaded')
            else:
                self.log.error('Login screen is not loaded')
        else:
            self.log.error('Problem - Not on New Landing screen')

        return self.global_contents.flag

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Landing screen from Register screen
        """

        self.global_contents.flag = False
        if self.driver.current_activity == self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME:
            if self.load_register_screen() == self.global_contents.REGISTER_ACTIVITY_NAME:
                self.driver.back()
                if self.global_contents.wait_for_android_activity_to_load(
                    self.driver,
                    self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
                ) == self.global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME:
                    self.global_contents.flag = True
                else:
                    self.log.error('New Landing screen is not loaded')
            else:
                self.log.error('Register screen is not loaded')
        else:
            self.log.error('Problem - Not on New Landing screen')

        return self.global_contents.flag
