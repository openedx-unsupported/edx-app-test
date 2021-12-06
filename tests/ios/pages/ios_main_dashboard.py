"""
    Main Dashboard Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage
from tests.ios.pages.ios_login import IosLogin


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

    def get_title_textview_portrait_mode(self):
        """
        Get screen title

        Returns:
            webdriver elements List: Screen title textview
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )[self.global_contents.first_existence]

    def get_profile_icon(self):
        """
        Get Profile Icon

        Returns:
            webdriver elements List: Profile icon
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.main_dashboard_profile_icon
        )

    def get_courses_tab(self):
        """
        Get Courses Tab

        Returns:
            webdriver elements List: Courses Tab
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_buttons
        )

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[self.global_contents.second_existence]

    def get_discovery_tab(self):
        """
        Get Discovery Tab

        Returns:
            webdriver elements List: Discovery tab
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[self.global_contents.fourth_existence]

    def get_programs_tab(self):
        """
        Get Programs Tab

        Returns:
            webdriver elements List: Programs tab
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[self.global_contents.third_existence]

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

    def load_profile_screen(self):
        """
        Load User Profile Screen

        Returns:
            webdriver element: Screen title textview
        """

        self.get_profile_icon().click()

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )[self.global_contents.third_existence]

    def load_discovery_tab(self):
        """
        Load Discovery

        Returns:
            webdriver elements : Discovery Tab textview
        """

        self.get_discovery_tab().click()

        return self.get_discovery_tab()

    def load_courses_tab(self):
        """
        Load Courses

        Returns:
            webdriver elements : Courses Tab textview
        """

        self.get_courses_tab().click()

        return self.get_courses_tab()

    def load_programs_tab(self):
        """
        Load Programs

        Returns:
            webdriver elements : Programs Tab textview
        """

        self.get_programs_tab().click()

        return self.get_programs_tab()

    def load_account_screen(self):
        """
        Load Account Screen

        Returns:
            webdriver element: Screen title textview
        """

        self.get_drawer_icon().click()

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )[1]

    def get_title_textview_landscape_mode(self):
        """
        Get screen title

        Returns:
            webdriver elements List: Screen title textview
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_otherviews
        )[self.global_contents.sixth_existence]

    def log_out(self):
        """
         Logout user

         Returns:
            webdriver element: Login screen Title Element
         """

        logout_option = self.global_contents.get_element_by_id(
            self.driver, ios_elements.profile_options_signout_button)
        logout_option.click()

        return IosLogin(self.driver, self.log).on_screen()

    def get_profile_close_button(self):
        """
        Get profile screen Close Icon

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_close_button
        )

    def get_acccount_close_button(self):
        """
        Get account screen Close Icon

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_options_close_button
        )

    def account_signout(self):
        """
        Get Sign out icon

        """

        signout_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.account_signout
        )

        return signout_element
