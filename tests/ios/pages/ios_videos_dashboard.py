"""
    Course Dashboard Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage
from tests.common import strings


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

        video_download_switch = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.video_dashboard_download_switch
        )

        return video_download_switch

    def get_video_download_header(self):
        """
        Get video download header

        Returns:
            webdriver element: video download header element
        """

        video_download_header = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.video_dashboard_download_header
        )

        return video_download_header

    def get_navigation_icon(self):
        """
        Wait for navigation icon

        Returns:
            webdriver element: Navigation icon
        """

        navigation_icon = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.video_subsection_navigation_icon
        )

        return navigation_icon

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

        course_item_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_item_title
        )

        return course_item_title

    def wait_for_all_videos_to_download(self, set_capabilities):
        """
        wait for all videos to download

        Arguments:
            set_capabilities (webdriver element): it will return driver object

        Returns:
            webdriver element: All videos downloaded element
        """

        video_tv_title = self.global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.video_dashboard_download_switch).get_attribute('label')

        while video_tv_title != strings.VIDEO_DASHBOARD_ALL_VIDEOS_DOWNLOADED_IOS:
            video_tv_title = self.global_contents.get_element_by_id(
                set_capabilities,
                ios_elements.video_dashboard_download_switch).get_attribute('label')

        return video_tv_title

    def check_videos_status(self, set_capabilities, status):
        """
        Get video status and check every video's status

        Arguments:
            set_capabilities (webdriver element): it will return driver object
            status (str): Downloading or Downloaded

        Returns:
            True if all videos status are same
            False if any single video status is not same
        """

        all_videos = self.global_contents.get_all_views_on_screen_by_id(
            set_capabilities,
            ios_elements.video_dashboard_downloaded_icon)

        self.global_contents.wait_and_get_element(
            set_capabilities,
            ios_elements.video_dashboard_downloaded_icon
        )

        return all(status in video_elem.text for video_elem in all_videos)

    def check_all_videos_numbers(self, set_capabilities):
        """
        Check video count is attached with every video

        Arguments:
            set_capabilities (webdriver element): it will return driver object

        Returns:
            True if video count is attached with every video
            False if video count is not attached with any video
        """

        all_videos = self.global_contents.get_all_elements_by_id(
            set_capabilities,
            ios_elements.video_dashboard_no_of_videos)

        return all(video_elem.text for video_elem in all_videos)
