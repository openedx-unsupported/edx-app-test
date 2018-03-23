"""
    Main Dashboard Page Module
"""

from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage


class AndroidMainDashboard(AndroidBasePage):
    """
    Main Dashboard screen
    """

    def on_screen(self):
        """
        Load Main Dashboard screen

        Returns:
            str: Main Dashboard screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        )

    def get_profile_icon(self):
        """
        Get profile icon

        Returns:
            webdriver element: profile icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_profile_icon
        )

    def get_title_textview(self):
        """
        Get screen title

        Returns:
            webdriver element: screen title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_screen_title
        )

    def get_menu_icon(self):
        """
        Get menu drawer icon

        Returns:
            webdriver element: menu drawer icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_menu_icon
        )

    def get_logout_account_option(self):
        """
        Click on menu drawer icon and get Account Menu Option

        Returns:
            webdriver element: Account Menu option
        """

        self.get_menu_icon().click()

        self.account_logout_option = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.account_logout_option
        )

        return self.account_logout_option

    def log_out(self):
        """
         Logout user

         Returns:
            str: Login screen Activity Name
         """

        self.account_logout_option.click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.NEW_LOGISTRATION_ACTIVITY_NAME
        )
