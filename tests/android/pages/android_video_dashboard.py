"""
    Video Dashboard page Module
"""
from tests.android.pages import android_elements
from tests.common import strings
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidVideoDasboard(AndroidBasePage):
    """
    Course Video Dashbaord screen
    """

    def check_videos_status(self, set_capabilities, status):
        """
        Get video status and check every video's status

        Returns:
            True if all videos status are same
            False if any single video status is not same
        """

        all_videos = self.global_contents.get_all_elements_by_id(
            set_capabilities,
            android_elements.video_dashboard_download_section)

        return all(video_elem.get_attribute('content-desc') == status for video_elem in all_videos)

    def wait_for_all_videos_to_download(self, set_capabilities):
        """
        wait for all videos to download

        Returns:
            webdriver element: All videos downloaded element
        """

        video_tv_title = self.global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_tv_title).text

        while video_tv_title != strings.VIDEO_DASHBOARD_ALL_VIDEOS_DOWNLOADED:
            video_tv_title = self.global_contents.get_element_by_id(
                set_capabilities,
                android_elements.video_dashboard_tv_title).text

        return video_tv_title

    def check_all_videos_numbers(self, set_capabilities):
        """
        Check video count is attached with every video

        Returns:
            True if video count is attached with every video
            False if video count is not attached with any video
        """

        all_videos = self.global_contents.get_all_elements_by_id(
            set_capabilities,
            android_elements.video_dashboard_no_of_videos)

        return all(video_elem.text for video_elem in all_videos)

    def wait_for_all_videos_to_delete(self, set_capabilities):
        """
        wait for all videos to delete

        Returns:
            webdriver element: Download to device element
        """

        video_tv_title = self.global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_tv_title).text

        while video_tv_title != strings.VIDEO_DASHBOARD_TV_TITLE:
            video_tv_title = self.global_contents.get_element_by_id(
                set_capabilities,
                android_elements.video_dashboard_tv_title).text

        return video_tv_title
