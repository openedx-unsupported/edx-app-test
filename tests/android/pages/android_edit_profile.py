"""
    Edit Profile Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidEditProfile(AndroidBasePage):
    """
    User Edit Profile screen
    """

    def change_birth_year_below_13(self):
        """
        Load edit profile screen
        Change birth year to below 13
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_change_birth_year
        )

        first_elem = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.edit_profile_change_birth_year
        )[0]

        last_elem = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.edit_profile_change_birth_year
        )[1]

        self.global_contents.scroll_screen(self.driver, first_elem, last_elem)

        elements = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.edit_profile_change_birth_year
        )

        for element in elements:
            if element.text == '2008':
                element.click()
                break

    def change_birth_year_above_13(self):
        """
        Load edit profile screen
        Change birth year to above 13

        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_change_birth_year
        )

        elements = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.edit_profile_change_birth_year
        )

        for element in elements:
            if element.text == '2007':
                element.click()
                break

    def get_by_class_from_elements(self, element_to_wait_for, screen_index):
        """
        Load edit profile screen
        Returns:
            webdriver element: Edit Profile choose photo options Element
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
            webdriver element: Edit Profile Image Element
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
            webdriver element: Edit Profile choose photo options Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            element_to_wait_for
        )
        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            element_to_wait_for
        )[screen_index]
