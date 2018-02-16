"""
    Main Dashboard Page Module
"""

from android.pages.android_base_page import AndroidBasePage
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

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews)[0]

    def get_drawer_icon(self):
        """
        Get menu drawer icon

        Returns:
            webdriver element: menu drawer icon Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_image_buttons
        )

    def get_drawer_account_option(self):
        """
        Click on menu drawer icon and get Account Menu Option

        Returns:
            webdriver element: Account Menu option
        """

        self.get_drawer_icon().click()

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashborad_drawer_account_textview
        )

    def log_out(self):
        """
         Logout user

         Returns:
            str: Login screen Activity Name
         """

        self.textview_drawer_account_option.click()
        textview_logout = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.account_logout_option)
        textview_logout.click()
        self.log.info(self.driver.current_activity)

        return self.driver.current_activity
