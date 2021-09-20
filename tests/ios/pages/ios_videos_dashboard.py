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
