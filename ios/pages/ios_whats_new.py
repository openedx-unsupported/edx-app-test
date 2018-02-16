"""
    Whats New Page Module
"""

from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


class IosWhatsNew(IosBasePage):
    """
    Whats New screen
    """

    def on_screen(self):
        """
        Load Whats New screen

        Returns:
            webdriver element:: Whats New screen Title element
        """

        return self.get_title_textview()

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
            webdriver element: Screen Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_title_textview
        )

    def get_close_button(self):
        """
        Get Close Icon

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_close_button
        )

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             webdriver element:  Main Image Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_main_image
        )

    def get_feature_title_textview(self):
        """
        Get Feature Title

        Returns:
             webdriver element: Feature Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_feature_title_textview
        )

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             webdriver element: Feature Details Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_feature_details_textview
        )

    def get_done_button(self):
        """
        Get Done

        Returns:
             webdriver element: Done Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_done_button
        )

    def exit_features(self):
        """
        Exit What New Screen/Features

        Returns:
            webdriver element:: Main Dashboard screen Title element
        """

        self.get_done_button().click()

        return self.driver.find_element_by_id(ios_elements.main_dashboard_title_textview)
