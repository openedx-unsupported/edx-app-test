"""
    New Logistration Page Module
"""

from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage
from common.globals import Globals


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

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_logistration_logo
        )

    def get_discover_course_button(self):
        """
        Get Discover Button

        Returns:
            webdriver element: Discover Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_logistration_discover_courses_button
        )

    def get_register_button(self):
        """
        Get Register Button

        Returns:
            webdriver element: Register Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_logistration_register_button
        )

    def get_signin_button(self):
        """
        Get Login Button

        Returns:
            webdriver element: Login Button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.new_logistration_sign_in_button
        )

    def get_screen_title_textview(self):
        """
        Get Register screen Title

        Returns:
            webdriver element: title element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews)[0]

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

    def load_discover_courses_screen(self):
        """
        Load Discover Courses Screen

        Returns:
             str: Discover Courses Activity Name
        """

        self.get_discover_course_button().click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.DISCOVERY_ACTIVITY_NAME
        )

    def back_and_forth_login(self):

        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Login screen
        """

        if self.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME:
            self.driver.back()
            return self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        else:
            self.log.error('Problem - Login screen is not loaded')
            return False

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Register screen
        """

        if self.load_register_screen() == Globals.REGISTER_ACTIVITY_NAME:
            self.driver.back()
            return self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        else:
            self.log.error('Problem - Register screen is not loaded')
            return False

    def back_and_forth_discover_courses(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on New Logistration screen from Discover Courses screen
        """

        if self.load_discover_courses_screen() == Globals.DISCOVERY_ACTIVITY_NAME:
            self.driver.back()
            return self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        else:
            self.log.error('Problem - Discovery screen is not loaded')
            return False
