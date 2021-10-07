"""
    Course Resources Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosCourseResources(IosBasePage):
    """
    Course Resources screen
    """

    def get_subsection_title(self):
        """
        Get share icon

        Returns:
            webdriver element: Share icon Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_textviews
        )

        all_textviews = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return all_textviews

    def get_navigation_back_icon(self):
        """
        Get share icon

        Returns:
            webdriver element: Share icon Element
        """

        all_buttons = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )
        return all_buttons
