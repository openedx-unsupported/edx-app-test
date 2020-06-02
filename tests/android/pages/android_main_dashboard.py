# coding=utf-8
"""
    Main Dashboard Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboard_profile_icon
        )

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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboard_menu_icon
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_menu_icon
        )

    def get_courses_tab(self):
        """
        Get Courses Tab

        Returns:
            webdriver element: Courses Tab Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboard_courses_tab
        )

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.main_dashboard_courses_tab
        )[self.global_contents.first_existence]

    def get_programs_tab(self):
        """
        Get Programs Tab

        Returns:
            webdriver element: Programs Tab Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.main_dashboard_discovery_tab
        )[self.global_contents.second_existence]

    def get_discovery_tab(self):
        """
        Get Discovery Tab

        Returns:
            webdriver element: Discovery Tab Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.main_dashboard_discovery_tab
        )[self.global_contents.third_existence]

    def load_discovery_tab(self):
        """
        Load Discovery Tab

        Returns:
            webdriver elements : Discovery Tab textview
        """

        self.get_discovery_tab().click()

        return self.get_discovery_tab()

    def load_courses_tab(self):
        """
        Load Courses Tab

        Returns:
            webdriver elements : Courses Tab textview
        """

        courses_tab = self.get_courses_tab()
        courses_tab.click()

        return self.get_courses_tab()

    def load_programs_tab(self):
        """
        Load Programs Tab

        Returns:
            webdriver elements : Programs Tab textview
        """

        Programs_tab = self.get_programs_tab()
        Programs_tab.click()

        return self.get_programs_tab().is_selected()

    def load_profile_screen(self):
        """
        Load Profile Screen

        Returns:
            str : Profile Screen Activity Name
        """

        self.get_profile_icon().click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.PROFILE_ACTIVITY_NAME
        )

    def load_account_screen(self):
        """
        Load Account Screen

        Returns:
            str : Account Screen Activity Name

        """

        self.get_menu_icon().click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.ACCOUNT_ACTIVITY_NAME
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

        self.account_logout_option = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.account_logout_option
        )

        self.account_logout_option.click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.NEW_LOGISTRATION_ACTIVITY_NAME
        )
