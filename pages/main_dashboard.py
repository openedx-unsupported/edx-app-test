"""
    Main Dashboard Page Module
"""

from time import sleep
from common.elements import Elements
from common.globals import Globals
from common.strings import Strings
from testdata.input_data import InputData


class MainDashboard:
    """
    Main Dashborad screen
    """

    def __init__(self, driver):
        self.elements = Elements()
        self.driver = driver
        self.global_contents = Globals()

    def on_screen(self):
        """
        Load Main Dashboard screen
        Returns:
            If Android - Main Dashboard screen Activity Name
            If iOS - Main Dashboard screen Title Name
        """

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(
                self.elements.main_dashboard_title_textview
            )
            return textview_screen_title

    def get_title_textview(self):
        """
        Get screen title
        Returns:
            screen title Element
        """

        if InputData.target_environment == Strings.ANDROID:
            all_textviews = self.global_contents.get_all_text_views(self.driver)
            textview_screen_title = all_textviews[0]
            return self.global_contents.validate_element(
                textview_screen_title,
                textview_screen_title.text,
                Strings.MAIN_DASHBOARD_SCREEN_TITLE,
                Strings.ERROR
            )

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(
                self.elements.main_dashboard_title_textview
            )
            return textview_screen_title

    def get_drawer_icon(self):
        """
        Get menu drawer icon
        Returns:
            menu drawer icon Element
        """

        if InputData.target_environment == Strings.ANDROID:
            all_image_buttons = self.global_contents.get_all_image_buttons(self.driver)
            image_button_drawer = all_image_buttons[0]
            return self.global_contents.validate_element(
                image_button_drawer,
                image_button_drawer.text,
                Strings.BLANK_FIELD,
                Strings.ERROR
            )

        elif InputData.target_environment == Strings.IOS:
            image_button_drawer = self.driver.find_element_by_class_name(
                self.elements.main_dashboard_navigation_icon
            )
            return image_button_drawer

    def get_drawer_account_option(self):
        """
        Click on menu drawer icon and get Account Menu Option
        Returns:
            Account Menu option
        """

        self.get_drawer_icon().click()
        sleep(self.global_contents.medium_timeout)

        if InputData.target_environment == Strings.ANDROID:
            self.textview_drawer_account_option = self.driver.find_element_by_id(
                self.elements.main_dashborad_drawer_account_textview
            )
            return self.global_contents.validate_element(
                self.textview_drawer_account_option,
                self.textview_drawer_account_option.text,
                Strings.MAIN_DASHBOARD_NAV_ACCOUNT_OPTION,
                Strings.ERROR
            )

        elif InputData.target_environment == Strings.IOS:
            self.textview_drawer_account_option = self.driver.find_element_by_id(
                self.elements.main_dashborad_drawer_account_textview
            )
            return self.textview_drawer_account_option

    def log_out(self):
        """
         Logout user
         Returns:
            If Android - Login screen Activity Name
            If iOS - Login screen Title Name
         """

        self.textview_drawer_account_option.click()
        sleep(self.global_contents.medium_timeout)

        if InputData.target_environment == Strings.ANDROID:
            textview_logout = self.driver.find_element_by_id(self.elements.account_logout_option)
            textview_logout.click()
            sleep(self.global_contents.medium_timeout)
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            textview_logout = self.driver.find_element_by_id(self.elements.account_logout_option)
            textview_logout.click()
            sleep(self.global_contents.medium_timeout)
            textview_screen_title = self.driver.find_element_by_id(self.elements.login_title_textview)
            return textview_screen_title