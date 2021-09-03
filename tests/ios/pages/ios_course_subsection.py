"""
    Course Subsection Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosCourseSubsection(IosBasePage):
    """
    Course Subsection screen
    """

    def get_subsection_title(self):
        """
        Get share icon

        Returns:
            webdriver element: Share icon Element
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

    def get_navigation_back_icon(self):
        """
        Get share icon

        Returns:
            webdriver element: Share icon Element
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )

    def account_signout(self):
        """
        Get Sign out icon

        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.account_signout
        )

    def get_course_subsection_header_label(self):
        """
        Get course section header

        Returns:
            webdriver element: course subsection header Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_section_header
        )

    def get_subsection_html_topic_title(self):
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
            ios_elements.course_subsection_download_icon
        )

    def get_subsection_component_title(self):
        """
        Get course item title

        Returns:
            webdriver element: course item title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_item_title
        )

    def get_subsection_component(self):
        """
        load subsection video component cell

        Returns:
            webdriver element: all subsection component title Elements
        """

        return self.global_contents.get_all_elements_by_id(
            self.driver,
            ios_elements.course_dashboard_course_item_title
        )
