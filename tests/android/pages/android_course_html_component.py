"""
    Course HTML component Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidCourseHTMLComponent(AndroidBasePage):
    """
    Course Dashboard screen
    """

    def get_course_navigation_back_icon(self):
        """
        Get Course Share icon

        Returns:
            webdriver element: Course share icon Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_html_component_navigation_icon
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_html_component_navigation_icon
        )

    def get_next_unit_title(self):
        """
        Load course Html component page

        Returns:
            webdriver element: Next unit title Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_html_component_next_unti_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_html_component_next_unti_title
        )

    def get_prev_unit_title(self):
        """
        Load course Html component page

        Returns:
            webdriver element: Prev unit title Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_html_component_prev_unti_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_html_component_prev_unti_title
        )

    def get_next_button(self):
        """
        Load course Html component page

        Returns:
            webdriver element: Next Button Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_html_component_goto_next_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_html_component_goto_next_button
        )

    def get_prev_button(self):
        """
        Load course Html component page

        Returns:
            webdriver element: Previous Button Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_html_component_goto_prev_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_html_component_goto_prev_button
        )

    def get_screen_activity_name(self):
        """
        Load course Html component page

        Returns:
            str: course Html component Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.COURSE_UNIT_NAVIGATION_ACTIVITY_NAME
        )
