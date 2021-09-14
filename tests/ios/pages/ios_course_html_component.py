"""
    Course html component Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosCourseHtmlComponent(IosBasePage):
    """
    Course Html component screen
    """

    def get_all_buttons(self):
        """
        Load html component screen

        Returns:
            webdriver element: All buttons
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_buttons
        )

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )

