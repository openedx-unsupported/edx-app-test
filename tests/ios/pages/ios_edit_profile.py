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

    def update_profile_elements(self, element_value):
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
            if element.get_attribute('value') == element_value:
                element.click()
                break

        return element_value

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

    def get_language_on_edit_profile(self):
        """
        Load edit profile screen
        return profile language
        """

        text_views = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        language_on_profile = text_views[8]

        return language_on_profile

    def change_user_info(self):
        """
        Load edit profile screen
        Change user About me information
        """

        about_me_element = self.global_contents.get_element_by_id(self.driver, ios_elements.edit_profile_about_me_text)
        about_me_element.clear()
        about_me_element.send_keys('Testing, This is my new info')

    def get_information_on_edit_profile(self):
        """
        Load edit profile screen
        return profile user information
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_textviews
        )

        text_views = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        information_on_profile = text_views[10]

        return information_on_profile
