# coding=utf-8

"""
    Profile Module
"""
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


    def on_screen(self):
        """
        Load Main Dashboard screen

        Returns:
            str: Main Dashboard Screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.ACCOUNT_ACTIVITY_NAME
        )


    def get_load_edit_profile_screen(self):
        """
        Load Edit Profile screen

        Returns:
            webdriver element: Edit Profile Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_edit_button
        )

    def get_edit_profile_activity_name(self):
        """
        Load Main Dashboard screen

        Returns:
            str: Main Dashboard Screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.EDIT_PROFILE_ACTIVITY_NAME
        )

    def get_user_profile_image(self):
        """
        Load Edit Profile screen

        Returns:
            webdriver element: User Image Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_avatar_icon
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_avatar_icon
        )

    def get_user_profile_name(self):
        """
        Load Edit Profile screen

        Returns:
            webdriver element: User Image Element
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
        Load Edit Profile screen

        Returns:
            webdriver element: User Image Element
        """

        # self.global_contents.wait_for_element_visibility(
        #     self.driver,
        #     android_elements.profile_screen_user_language
        # )

        language_variable = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_language
        )

        if language_variable:
            print('inside if:')
            return self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.profile_screen_user_language
            )
        else:
            print('inside Else:')
            return None

    def get_user_profile_bio(self):
        """
        Load Edit Profile screen

        Returns:
            webdriver element: User Image Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_location
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_location
        )

    def get_user_profile_location(self):
        """
        Load Edit Profile screen

        Returns:
            webdriver element: User Image Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_user_bio
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_user_bio
        )
    # def get_profile_row(self):
    #     """
    #     Get Profile Row

    #     Returns:
    #         webdriver element: Profile Element
    #     """

    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         android_elements.account_profile_option
    #     )

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         android_elements.account_profile_option
    #     )

    # def load_profile_activity(self):
    #     """
    #     Get Profile Row

    #     Returns:
    #         webdriver element: Profile Screen activity
    #     """

    #     self.get_profile_row().click()

    #     return self.global_contents.wait_for_android_activity_to_load(
    #         self.driver,
    #         self.global_contents.PROFILE_ACTIVITY_NAME
    #     )

    # def get_settings_row(self):
    #     """
    #     Get Settings Row

    #     Returns:
    #         webdriver element: Settings Element
    #     """

    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         android_elements.account_settings_option
    #     )

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         android_elements.account_settings_option
    #     )

    # def load_settings_activity(self):
    #     """
    #     Get Settings Row

    #     Returns:
    #         webdriver element: Settings Screen activity
    #     """

    #     self.get_settings_row().click()

    #     return self.global_contents.wait_for_android_activity_to_load(
    #         self.driver,
    #         self.global_contents.SETTINGS_ACTIVITY_NAME
    #     )

    # def get_submit_feedback_row(self):
    #     """
    #     Get Submit Feedback Row

    #     Returns:
    #         webdriver element: Submit_Feedback Element
    #     """

    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         android_elements.submit_feedback_option
    #     )

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         android_elements.submit_feedback_option
    #     )

    # def get_logout_row(self):
    #     """
    #     Get Logout Row

    #     Returns:
    #         webdriver element: Logout Element
    #     """

    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         android_elements.account_logout_option
    #     )

    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         android_elements.account_logout_option
    #     )

    # def get_navigation_icon(self):
    #     """
    #     Get menu drawer icon

    #     Returns:
    #         webdriver element: menu drawer icon Element
    #     """

    #     self.global_contents.wait_for_element_visibility(
    #         self.driver,
    #         android_elements.course_dashboard_navigation_icon
    #     )

    #     return self.global_contents.get_all_views_on_screen(
    #         self.driver,
    #         android_elements.course_dashboard_navigation_icon
    #     )[0]

    # def on_screen(self):
    #     """
    #     Load Main Dashboard screen

    #     Returns:
    #         str: Main Dashboard Screen Activity Name
    #     """

    #     return self.global_contents.wait_for_android_activity_to_load(
    #         self.driver,
    #         self.global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
    #     )
