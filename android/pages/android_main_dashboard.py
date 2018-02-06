"""
    Main Dashboard Page Module
"""

from time import sleep

from android.pages.android_base_page import AndroidBasePage
from common.globals import Globals
from common import strings
from android.pages import android_elements


class AndroidMainDashboard(AndroidBasePage):
    """
    Main Dashborad screen
    """

    def on_screen(self):
        """
        Load Main Dashboard screen

        Returns:
            str: Main Dashboard screen Activity Name
        """

        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def get_title_textview(self):
        """
        Get screen title

        Returns:
            webdriver element: screen title Element
        """

        all_textviews = self.global_contents.get_all_views(self.driver, android_elements.all_textviews)
        textview_screen_title = all_textviews[0]
        return self.global_contents.validate_element(
            textview_screen_title,
            textview_screen_title.text,
            strings.MAIN_DASHBOARD_SCREEN_TITLE,
            strings.ERROR
        )

    def get_drawer_icon(self):
        """
        Get menu drawer icon

        Returns:
            webdriver element: menu drawer icon Element
        """

        all_image_buttons = self.global_contents.get_all_views(self.driver, android_elements.all_image_buttons)
        image_button_drawer = all_image_buttons[0]
        return self.global_contents.validate_element(
            image_button_drawer,
            image_button_drawer.text,
            strings.BLANK_FIELD,
            strings.ERROR
        )

    def get_drawer_account_option(self):
        """
        Click on menu drawer icon and get Account Menu Option

        Returns:
            webdriver element: Account Menu option
        """

        self.get_drawer_icon().click()
        sleep(self.global_contents.medium_timeout)

        self.textview_drawer_account_option = self.driver.find_element_by_id(
            android_elements.main_dashborad_drawer_account_textview
        )
        return self.global_contents.validate_element(
            self.textview_drawer_account_option,
            self.textview_drawer_account_option.text,
            strings.MAIN_DASHBOARD_NAV_ACCOUNT_OPTION,
            strings.ERROR
        )

    def log_out(self):
        """
         Logout user

         Returns:
            str: Login screen Activity Name
         """

        self.textview_drawer_account_option.click()
        sleep(self.global_contents.medium_timeout)
        textview_logout = self.driver.find_element_by_id(android_elements.account_logout_option)
        textview_logout.click()
        sleep(self.global_contents.medium_timeout)
        self.log.info(self.driver.current_activity)
        return self.driver.current_activity
