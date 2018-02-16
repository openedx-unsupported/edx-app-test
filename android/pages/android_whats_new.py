"""
    Whats New Page Module
"""

from android.pages.android_base_page import AndroidBasePage
from android.pages import android_elements


class AndroidWhatsNew(AndroidBasePage):
    """
    Whats New screen
    """

    def on_screen(self):
        """
        Load Whats New screen

        Returns:
            str: Whats New Activity Name
        """

        self.log.info(self.driver.current_activity)

        return self.driver.current_activity

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
             webdriver element: Screen Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_title_textview
        )

    def get_cross_icon(self):
        """
        Get Cross Icon

        Returns:
             webdriver element: Cross Icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_close_button)

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             webdriver element: Main Image Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_main_image
        )

    def get_feature_title_textview(self):
        """
        Get Feature Title

        Returns:
             webdriver element: Feature Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_feature_title_textview
        )

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             webdriver element: Feature Details Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_feature_details_textview
        )

    def get_done_button(self):
        """
        Get Done

        Returns:
             webdriver element: Done Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_done_button
        )

    def exit_features(self):
        """
        Exit What New Screen/Features

        Returns:
             str: Main Dashboard Activity Name
        """

        self.get_done_button().click()
        self.log.info(self.driver.current_activity)

        return self.driver.current_activity
