# coding=utf-8

"""
    Course Videos Dashboard Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidVideosDashboard(AndroidBasePage):
    """
    Course Dashboard screen
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
        
    def get_video_dashboard_tv_title(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard tv title element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_tv_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_tv_title
        )
        
    def get_video_dashboard_tv_subtitle(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard tv Sub-title element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_tv_subtitle
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_tv_subtitle
        )

    def get_video_dahboard_video_icon(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video icon element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dahboard_video_icon
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dahboard_video_icon
        )

    def get_video_dashboard_bulk_download_toggle(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video icon element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_bulk_download_toggle
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_bulk_download_toggle
        )

    def get_video_dashboard_download_bar(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard download bar element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_download_bar
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_download_bar
        )
        
    def get_video_dashboard_bulk_download_toggle(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard bulk download toggle element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_bulk_download_toggle
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_bulk_download_toggle
        )
        
    def get_video_dashboard_download_bar(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard download bar element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_download_bar
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_download_bar
        )

    def get_video_dashboard_bulk_download(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard bulk download element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_bulk_download
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_bulk_download
        )

    def get_video_download_permission_allow_button(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard download permission allow button element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_download_permission_allow_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_download_permission_allow_button
        )

    def get_video_dashboard_all_downloading_spinner(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard all videos downloading spinner element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_all_downloading_spinner
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_all_downloading_spinner
        )

    def get_video_dashboard_section_download_spinner(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard section download spinner element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_section_download_spinner
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_section_download_spinner
        )

    def get_video_dashboard_download_progress_wheel(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard download progress wheel element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_download_progress_wheel
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_download_progress_wheel
        )

    def get_video_dashboard_no_of_videos(self):
        """
        Load Video Dashboard

        Returns:
            "Webdriver element: Video dashboard number of videos element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_dashboard_no_of_videos
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.video_dashboard_no_of_videos
        )
