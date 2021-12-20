"""
    Edit Profile Page Module
"""

from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage
from tests.common import strings


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

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return all_textviews_on_screen[1]

    def change_new_location(self, setup_logging):
        """
        Load edit profile screen
        Change user profile location
        """

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        for element in all_textviews_on_screen:
            if (element.get_attribute('value') == strings.EDIT_PROFILE_NEW_LOCATION):
                element.click()
                break
            else:
                setup_logging.info('-- Finding new location')

        return strings.EDIT_PROFILE_NEW_LOCATION

    def check_location_on_edit_profile(self):
        """
        Load edit profile screen
        return profile location
        """

        all_textviews_on_edit_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        location_on_profile = all_textviews_on_edit_screen[6]

        return location_on_profile

    def change_old_location(self, setup_logging):
        """
        Load edit profile screen
        Change user profile location
        """

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        for element in all_textviews_on_screen:
            if (element.get_attribute('value') == strings.EDIT_PROFILE_OLD_LOCATION):
                element.click()
                break
            else:
                setup_logging.info('-- Finding Old location')

        return strings.EDIT_PROFILE_OLD_LOCATION

    def change_new_language(self, setup_logging):
        """
        Load edit profile screen
        Change user profile language
        """

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        for element in all_textviews_on_screen:
            if (element.get_attribute('value') == strings.EDIT_PROFILE_USER_NEW_LANGUAGE):
                element.click()
                break
            else:
                setup_logging.info('-- Finding New language')

        return strings.EDIT_PROFILE_USER_NEW_LANGUAGE

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

    def change_old_language(self, setup_logging):
        """
        Load edit profile screen
        Change user profile location
        """

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        for element in all_textviews_on_screen:
            if (element.get_attribute('value') == strings.EDIT_PROFILE_USER_OLD_LANGUAGE):
                element_located_selection_state_to_be.click()
                break
            else:
                setup_logging.info('-- Finding Old language')

        return strings.EDIT_PROFILE_USER_OLD_LANGUAGE

    def change_user_info(self):
        """
        Load edit profile screen
        Change user About me information
        """

        about_me_element = self.global_contents.get_element_by_id\
            (self.driver, ios_elements.edit_profile_about_me_text_area)
        about_me_element.click()
        about_me_element.clear()
        about_me_element.send_keys('Testing, This is my new info')

    def check_information_on_edit_profile(self):
        """
        Load edit profile screen
        return profile user information
        """

        all_textviews_on_edit_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        information_on_profile = all_textviews_on_edit_screen[10]

        return information_on_profile
