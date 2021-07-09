"""
    Course Dashboard Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosCourseDashboard(IosBasePage):
    """
    Course Dashboard screen
    """

    def get_share_icon(self):
        """
        Get share icon

        Returns:
            webdriver element: Share icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dahsboard_share_icon
        )

    def get_course_image(self):
        """
        Get course image

        Returns:
            webdriver element: course image Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_image
        )

    def get_course_title(self):
        """
        Get course title

        Returns:
            webdriver element: course title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_title
        )

    def get_course_date(self):
        """
        Get course date

        Returns:
            webdriver element: course date Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_date
        )

    def get_course_header_outline(self):
        """
        Get course header outline

        Returns:
            webdriver element: course header outline Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_header_outline
        )

    def get_course_header_subtitle(self):
        """
        Get course header subtitle

        Returns:
            webdriver element: course header subtitle Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_header_subtitle
        )

    def get_course_section_header(self):
        """
        Get course section header

        Returns:
            webdriver element: course section header Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_section_header
        )

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

    def get_course_item_download_icon(self):
        """
        Get course item download icon

        Returns:
            webdriver element: course item download icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_item_download
        )

    def get_courses_tab(self):
        """
        Get course tab

        Returns:
            webdriver element: course tab Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_courses_tab
        )

    def get_videos_tab(self):
        """
        Get videos tab

        Returns:
            webdriver element: videos tab Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_videos_tab
        )

    def get_discussion_tab(self):
        """
        Get discussion tab

        Returns:
            webdriver element: discussion tab Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_discussion_tab
        )

    def get_dates_tab(self):
        """
        Get dates tab

        Returns:
            webdriver element: dates tab Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_dates_tab
        )

    def get_resources_tab(self):
        """
        Get resources tab

        Returns:
            webdriver element: resources tab Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_resources_tab
        )

    def load_courses_tab(self):
        """
        Get courses tab

        Returns:
            webdriver element: course tab Element
        """

        self.get_courses_tab().click()

    def load_resources_tab(self):
        """
        Get resources tab

        Returns:
            webdriver element: resources tab Element
        """

        self.get_resources_tab().click()

    def load_videos_tab(self):
        """
        Get Videos tab

        Returns:
            webdriver element: Videos tab Element
        """

        self.get_videos_tab().click()

    def load_discussion_tab(self):
        """
        Get Discussion tab

        Returns:
            webdriver element: Discussion tab Element
        """

        self.get_discussion_tab().click()

    def load_dates_tab(self):
        """
        Get Dates tab

        Returns:
            webdriver element: Dates tab Element
        """

        self.get_dates_tab().click()

    def get_handouts_row_title(self):
        """
        Get handouts row title

        Returns:
            webdriver element: handouts row title Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_title
        )[0]

    def get_handouts_row_name(self):
        """
        Get handouts row name

        Returns:
            webdriver element: handouts row name Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_name
        )[0]

    def get_announcements_row_title(self):
        """
        Get announcements row title

        Returns:
            webdriver element: announcements row title Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_title
        )[1]

    def get_announcements_row_name(self):
        """
        Get announcements row name

        Returns:
            webdriver element: announcements row name Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_name
        )[1]

    def load_handouts_row(self):
        """
        Load handouts row name

        Returns:
            webdriver element: handouts row name Element
        """

        self.get_handouts_row_title().click()

    def load_announcement_row(self):
        """
        Load announcement row name

        Returns:
            webdriver element: announcement row name Element
        """

        self.get_announcements_row_title().click()
