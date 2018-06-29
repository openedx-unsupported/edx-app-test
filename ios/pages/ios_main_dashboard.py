"""
    Main Dashboard Page Module
"""

from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage
from ios.pages.ios_login import IosLogin


class IosMainDashboard(IosBasePage):
    """
    Main Dashboard screen
    """

    def get_drawer_icon(self):
        """
        Get menu drawer icon

        Returns:
            webdriver element: menu drawer icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.main_dashboard_navigation_icon
        )

    def get_account_options(self):
        """
        Click on menu drawer icon and get Account Options

        Returns:
            webdriver elements List: Account Options
        """

        self.get_drawer_icon().click()
        self.account_options = self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.account_options
        )

        return self.account_options

    def log_out(self):
        """
         Logout user

         Returns:
            webdriver element: Login screen Title Element
         """

        logout_option = self.account_options[self.LOGOUT_OPTION]
        logout_option.click()

        return IosLogin(self.driver, self.log).on_screen()
