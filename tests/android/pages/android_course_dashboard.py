"""
    Course Dashboard Module
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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_share_icon
        )

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

    def get_resume_course_bar(self):
        """
        Get course last access view

        Returns:
            webdriver element: course last access Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_resume_course_bar
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_resume_course_bar
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

    def course_dashboard_toolbar_dismiss_button(self):
        """
        Get course dashboard toolbar dismiss button

        Returns:
            "Webdriver element: Course dashboard toolbar dismiss"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_toolbar_dismiss_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_toolbar_dismiss_button
        )

    def course_dashboard_course_title(self):
        """
        Get course dashboard title

        Returns:
            "Webdriver element: Course dashboard title element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_course_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_title
        )

    def course_dashboard_course_organization(self):
        """
        Get course dashboard organization

        Returns:
            "Webdriver element: Course dashboard organization element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_course_organization
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_organization
        )

    def course_dashboard_course_organization(self):
        """
        Get course dashboard organization

        Returns:
            "Webdriver element: Course dashboard organization element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_course_organization
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_organization
        )

    def course_dashboard_course_expiry_date(self):
        """
        Get course dashboard course expiry date

        Returns:
            "Webdriver element: Course dashboard course expiry date element"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_course_expiry_date
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_expiry_date
        )

    def course_dashboard_get_all_tabs(self):
        """
        Get course dashboard all tabs

        Returns:
            "Webdriver element: Course dashboard all tabs array"
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_layout
        )

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.course_layout
        )
