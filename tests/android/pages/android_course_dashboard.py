# coding=utf-8

"""
    Discovery Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidCourseDashboard(AndroidBasePage):
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

    def get_all_text_views(self):
        """"
        Get text_view element

        Returns:
            "Webdriver elements: all text_views"

        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )

    def get_course_share_icon(self):
        """
        Get Course Share icon

        Returns:
            "Webdriver element: Course share icon element"
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_share_icon
        )

    def get_course_tab(self):
        """
        Get Course Tab

        Returns:
            "Webdriver element: Course tab element"
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_tab
        )

    def get_videos_tab(self):
        """
        Get Videos Tab

        Returns:
            "Webdriver element: Video tab element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_videos_tab
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_videos_tab
        )

    def get_discussion_tab(self):
        """
        Get discussion Tab

        Returns:
            "Webdriver element: discussion tab element"
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_discussion_tab
        )

    def get_dates_tab(self):
        """
        Get dates Tab

        Returns:
            "Webdriver element: dates tab element"
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_dates_tab
        )

    def get_resources_tab(self):
        """
        Get resources Tab

        Returns:
            "Webdriver element: resources tab element"
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_resources_tab
        )

    def get_course_image(self):
        """
        Get course image

        Returns:
            webdriver element: course image Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_image
        )

    def get_course_name(self):
        """
        Get course name

        Returns:
            webdriver element: course name Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_course_name
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_name
        )

    def get_course_date(self):
        """
        Get course date

        Returns:
            webdriver element: course date Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_date
        )

    def get_course_last_access_row(self):
        """
        Get course last access view

        Returns:
            webdriver element: course last access Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_last_accessed
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_last_accessed
        )

    def get_course_content_header(self):
        """
        Get course content header

        Returns:
            webdriver element: course content header Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_content_header
        )
