from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidProfile(AndroidBasePage):
    """
    User Profile screen
    """

    def get_navigation_icon(self):
        """
        Get menu drawer icon

        Returns:
            webdriver element: menu drawer icon Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_navigation_icon
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.course_dashboard_navigation_icon
        )[0]

    def get_account_activity(self):
        """
        Load Account screen

        Returns:
            str: Account Screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.ACCOUNT_ACTIVITY_NAME
        )

    def get_edit_profile_screen(self):
        """
        Get Edit Profile screen

        Returns:
            webdriver element: Edit Profile Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_edit_button
        )

    def get_user_profile_image(self):
        """
        Load Profile screen

        Returns:
            webdriver element: User Image Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_image
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_image
        )

    def get_user_profile_name(self):
        """
        Load Profile screen

        Returns:
            webdriver element: User Name Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_name
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_name
        )

    def get_user_profile_language(self):
        """
        Get User Profile Language

        Returns:
            webdriver element: User Profile language Element (If language selected)
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_language
        )

        language_variable = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_language
        )

        if language_variable:
            return self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.profile_screen_user_language
            )

    def get_limited_profile_view(self):
        """
        Load Profile screen

        Returns:
            webdriver element: Limited sharing Element (If limited profile shared)
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_limited_view
        )

        limited_view = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_limited_view
        )

        if limited_view:
            return self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.profile_screen_limited_view
            )

    def get_user_profile_location(self):
        """
        Get user Profile location

        Returns:
            webdriver element: User Location Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_location
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_location
        )

    def get_user_profile_bio(self):
        """
        Get User Profile bio

        Returns:
            webdriver element: User Bio Text Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_bio
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_bio
        )

    def get_profile_age_text_note(self):
        """
        Get profile age text

        Returns:
              webdriver element: Profile age Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews)[self.global_contents.fifth_existence]

    def get_profile_account_settings_button(self):
        """
        Get Account settings button in profile screen

        Returns:
            webdriver element: Account settings Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_account_settings_btn
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_account_settings_btn
        )
