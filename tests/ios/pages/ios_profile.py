"""
    Profile Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosProfile(IosBasePage):
    """
    Profile screen
    """

    def get_personal_information_profile_cell(self):
        """
        Get Personal information profile cell

        Returns:
            webdriver element: Personal information profile Element
        """

        personal_information_cell = self.global_contents.get_element_by_id(
            self.driver,
            ios_elements.personal_information_profile_cell
        )

        return personal_information_cell

    def get_subsection_title(self):
        """
        Wait for all textview on screen
        Returns:
            webdriver element: Subsection title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_textviews
        )

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return all_textviews_on_screen[1]

    def get_navigation_icon(self):
        """
        Wait for navigation icon
        Returns:
            webdriver element: Navigation icon
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_buttons
        )

        all_icons = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons)

        navigation_icon = all_icons[self.global_contents.first_existence]

        return navigation_icon

    def get_profile_screen_edit_profile_button(self):
        """
        Get Profile screen edit profile button

        Returns:
            webdriver element: edit profile button Element
        """

        edit_profile_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_edit_profile_button
        )

        return edit_profile_button

    def get_profile_screen_username_label(self):
        """
        Get Profile screen user name label

        Returns:
            webdriver element: user name Element
        """

        user_name_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_username_label
        )

        return user_name_element

    def get_profile_screen_language_label(self):
        """
        Get Profile screen language label

        Returns:
            webdriver element: language Element
        """

        language_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_language_label
        )

        return language_element

    def get_profile_screen_country_label(self):
        """
        Get Profile screen country label

        Returns:
            webdriver element: country Element
        """

        country_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_country_label
        )

        return country_element

    def get_profile_screen_bio_text(self):
        """
        Get Profile screen bio label

        Returns:
            webdriver element: profile's bio Element
        """

        personal_bio_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_bio_text
        )

        return personal_bio_element

    def get_profile_screen_limited_view_message(self):
        """
        Get Profile screen bio label

        Returns:
            webdriver element: profile's bio Element
        """

        limited_view_message_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_limited_view_message
        )

        return limited_view_message_element

    def get_edit_profile_back_icon(self):
        """
        Get Profile screen edit profile button

        Returns:
            webdriver element: edit profile button Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_back_icon
        )

    def get_profile_back_icon(self):
        """
        Get Profile screen edit profile button

        Returns:
            webdriver element: edit profile button Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_screen_edit_profile_back_icon
        )

    def get_back_icon(self):
        """
        Wait for back icon
        Returns:
            webdriver element: back icon
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_buttons
        )

        all_icons = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons)

        back_icon = all_icons[self.global_contents.second_existence]

        return back_icon
