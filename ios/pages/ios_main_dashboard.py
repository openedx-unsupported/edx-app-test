"""
    Main Dashboard Page Module
"""

from time import sleep
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


class IosMainDashboard(IosBasePage):
    """
    Main Dashborad screen
    """

    def on_screen(self):
        """
        Load Main Dashboard screen

        Returns:
            str: Main Dashboard screen Title Name
        """

        return self.driver.find_element_by_id(
            ios_elements.main_dashboard_title_textview
        )

    def get_title_textview(self):
        """
        Get screen title

        Returns:
            webdriver element: screen title Element
        """

        return self.driver.find_element_by_id(
            ios_elements.main_dashboard_title_textview
        )

    def get_drawer_icon(self):
        """
        Get menu drawer icon

        Returns:
            webdriver element: menu drawer icon Element
        """

        return self.driver.find_element_by_class_name(ios_elements.main_dashboard_navigation_icon)

    def get_drawer_account_option(self):
        """
        Click on menu drawer icon and get Account Menu Option

        Returns:
            webdriver element: Account Menu option
        """

        self.get_drawer_icon().click()
        sleep(self.global_contents.medium_timeout)

        self.textview_drawer_account_option = self.driver.find_element_by_id(
            ios_elements.main_dashborad_drawer_account_textview
            )
        return self.textview_drawer_account_option

    def log_out(self):
        """
         Logout user

         Returns:
            str: Login screen Title Name
         """

        self.textview_drawer_account_option.click()
        sleep(self.global_contents.medium_timeout)
        textview_logout = self.driver.find_element_by_id(ios_elements.account_logout_option)
        textview_logout.click()
        sleep(self.global_contents.medium_timeout)
        textview_screen_title = self.driver.find_element_by_id(ios_elements.login_title_textview)
        return textview_screen_title