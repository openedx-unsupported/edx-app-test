"""
    Edit Profile Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosEditProfile(IosBasePage):
    """
    Edit Profile screen
    """

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

        text_views = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return text_views[1]

    def update_location_and_language(self, user_profile_data):
        """
        Load edit profile screen
        update location or language
        Returns:
            webdriver element: location or language element
        """

        text_views = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        for element in text_views:
            if element.get_attribute('value') == user_profile_data:
                element.click()
                break

        return user_profile_data

    def get_location_on_edit_profile(self):
        """
        Load edit profile screen
        return profile location
        """

        text_views = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        location_on_profile = text_views[6]

        return location_on_profile

    def check_language_on_edit_profile(self):
        """
        Load edit profile screen
        return profile language
        """

        all_textviews_on_edit_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        language_on_profile = all_textviews_on_edit_screen[8]

        return language_on_profile

    def change_user_info(self):
        """
        Load edit profile screen
        Change user About me information
        """

        about_me_element = self.global_contents.get_element_by_id(self.driver, ios_elements.edit_profile_about_me_text)
        about_me_element.clear()
        about_me_element.send_keys('Testing, This is my new info')

    def check_information_on_edit_profile(self):
        """
        Load edit profile screen
        return profile user information
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_textviews
        )

        all_textviews_on_edit_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        information_on_profile = all_textviews_on_edit_screen[10]

        return information_on_profile
