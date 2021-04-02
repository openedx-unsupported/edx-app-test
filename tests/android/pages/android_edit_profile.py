"""
    Edit Profile Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidEditProfile(AndroidBasePage):
    """
    User Account screen
    """

    def get_edit_profile_screen_title(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Title Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )[0]

    def get_edit_profile_image(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile Image Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_screen_image
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_screen_image
        )

    def get_edit_profile_user_name(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile User Name Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_user_name
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_user_name
        )

    def get_edit_profile_change_photo(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile change photo Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_change_photo
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_change_photo
        )

    def get_edit_profile_label(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile label Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_label
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_label
        )

    def get_edit_profile_full_view(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile full view Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_full_view
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_full_view
        )

    def get_edit_profile_limited_view(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile limited view Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_limited_view
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_limited_view
        )

    def get_edit_profile_instructions(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Edit Profile Instructions Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_instructions
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_instructions
        )

    def get_edit_profile_birth_year(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Birth year Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )[5]

    def get_edit_profile_location(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Location Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )[6]

    def get_edit_profile_language(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: Language Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )[7]

    def get_edit_profile_about_me(self):
        """
        Load edit profile screen

        Returns:
            webdriver element: About me Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )[8]
