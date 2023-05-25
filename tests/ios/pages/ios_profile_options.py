"""
    Profile Options Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosProfileOptions(IosBasePage):
    """
    Profile Options screen
    """

    def get_all_textviews(self):
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

        return all_textviews_on_screen

    def get_all_buttons(self):
        """
        Load Profile options screen

        Returns:
            webdriver element: All buttons
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_buttons
        )

        all_buttons_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )

        return all_buttons_on_screen
