"""
    Course Dashboard Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosVideosDashboard(IosBasePage):
    """
    Course Dashboard screen
    """

    def get_video_download_switch(self):
        """
        Get video download switch

        Returns:
            webdriver element: video download switch element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.video_dashboard_download_switch
        )

    def get_video_download_header(self):
        """
        Get video download header

        Returns:
            webdriver element: video download header element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.video_dashboard_download_header
        )

    def get_navigation_icon(self):
        """
        Wait for navigation icon

        Returns:
            webdriver element: Navigation icon
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.video_subsection_navigation_icon
        )

    def get_subsection_title(self):
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

        return all_textviews_on_screen[0]

    def get_course_item_title(self):
        """
        Get course item title

        Returns:
            webdriver element: course item title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_item_title
        )
