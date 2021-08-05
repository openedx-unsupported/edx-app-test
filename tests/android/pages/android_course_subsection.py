"""
    Course Subsection page Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidCourseSubsection(AndroidBasePage):
    """
    Course Dashboard screen
    """

    def get_course_row_header(self):
        """
        Get course content header

        Returns:
            webdriver element: Course content header Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_row_header
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_row_header
        )

    def get_course_navigation_icon(self):
        """
        Get Course Share icon

        Returns:
            webdriver element: Course share icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_topic_navigation_icon
        )

    def on_screen(self):
        """
        Load Course Dashboard screen

        Returns:
            str: Course Dashboard Screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
        )

    def get_topic_download_icon(self):
        """
        Get course download icon

        Returns:
            webdriver element: Course video download icon
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.course_dashboard_download_icon
        )[self.global_contents.first_existence]

    def get_course_topic_icon(self):
        """
        Get course topic icon

        Returns:
            webdriver element: Course topic icon
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.course_topic_icon
        )[self.global_contents.first_existence]

    def get_course_video_icon(self):
        """
        Get course video icon

        Returns:
            webdriver element: Course video icon
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.course_topic_icon
        )[self.global_contents.second_existence]

    def get_course_topic_row(self):
        """
        Get course topic element

        Returns:
            webdriver element: course topic Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_row_header
        )

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.course_dashboard_row_header
        )[self.global_contents.first_existence]

    def get_course_video_row(self):
        """
        Get course video

        Returns:
            webdriver element: course content video Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_row_header
        )

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.course_dashboard_row_header
        )[self.global_contents.second_existence]

    def navigate_to_main_dashboard(self, set_capabilities):
        """
        Get navigation icon and navigate to main dashboard screen to logout

        """

        set_capabilities.back()
        set_capabilities.back()
        set_capabilities.back()
