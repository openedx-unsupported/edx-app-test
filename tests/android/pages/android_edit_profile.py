"""
    Edit Profile Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidEditProfile(AndroidBasePage):
    """
    User Edit Profile screen
    """

    def get_by_class_from_elements(self, element_to_wait_for, screen_index):
        """
        Load edit profile screen
        Returns:
            webdriver element from screen by class name of given index
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            element_to_wait_for
        )
        return self.global_contents.get_all_views_on_screen(
            self.driver,
            element_to_wait_for
        )[screen_index]

    def get_element_by_id(self, element_id):
        """
        Load edit profile screen

        Returns:
            webdriver element of given id
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            element_id
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            element_id
        )

    def get_by_id_from_elements(self, element_to_wait_for, screen_index):
        """
        Load edit profile screen
        Returns:
            webdriver element from screen by id of given index
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            element_to_wait_for
        )
        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            element_to_wait_for
        )[screen_index]

    def change_user_location(self):
        """
        Load edit profile screen
        Change user profile location

        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_change_location
        )

        return self.global_contents.get_all_elements_by_id(
            self.driver,
            android_elements.edit_profile_change_location
        )[1]

    def change_user_language(self):
        """
        Load edit profile screen
        Change user language

        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_change_language
        )

        return self.global_contents.get_all_elements_by_id(
            self.driver,
            android_elements.edit_profile_change_language
        )

    def change_user_info(self):
        """
        Load edit profile screen
        Change user information

        """

        self.get_user_info_text_area().click()
        self.get_user_info_text_area().clear()
        self.get_user_info_text_area().send_keys('Testing, This is my new info')

        self.global_contents.get_element_by_id(
            self.driver,
            android_elements.edit_profile_about_me_sumit_button
        ).click()

    def get_user_info_text_area(self):
        """
        Load edit profile screen
        Get user information text area

        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_about_me_text_area
        )

        return self.global_contents.get_element_by_id(
            self.driver,
            android_elements.edit_profile_about_me_text_area
        )
