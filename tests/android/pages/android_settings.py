"""
    Settings page Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidSettings(AndroidBasePage):
    """
    User Settings screen
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
        Load Settings screen

        Returns:
            str: Settings Screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.SETTINGS_ACTIVITY_NAME
        )

    def get_settings_text(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: wifi only download element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_text
        )

    def get_download_content_text(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: Download content element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_download_content_text
        )

    def get_settings_wifi_toggle(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: settings_wifi_toggle element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_wifi_toggle
        )

    def get_allow_cellular_download_dialog(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: Allow Cellular download dialoug element
        """

        self.get_settings_wifi_toggle().click()

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.settings_screen_allow_cellular_download_dialog
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_allow_cellular_download_dialog
        )

    def get_dialog_title(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: Dialog Title element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_dialog_title
        )

    def get_dialog_message(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: Dialoug Message element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_dialog_message
        )

    def get_dialog_dont_allow_button(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: Dialoug dont allow button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_dialog_dont_allow_button
        )

    def get_dialog_allow_button(self):
        """
        Load Settings Screen

        Returns:
            webdriver element: Dialoug allow button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.settings_screen_dialog_allow_button
        )

    def check_dont_allow_button(self):
        """
        Load Dialog Screen

        Returns:
            webdriver element: settings_wifi_toggle element
        """

        self.get_dialog_dont_allow_button().click()

        return self.get_settings_wifi_toggle()

    def check_allow_button(self):
        """
        Load Dialog Screen

        Returns:
            webdriver element: settings_wifi_toggle element
        """

        self.get_settings_wifi_toggle().click()
        self.get_dialog_allow_button().click()

        return self.get_settings_wifi_toggle()
