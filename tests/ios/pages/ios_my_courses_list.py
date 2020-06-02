# coding=utf-8

"""
    My Courses List Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosMyCoursesList(IosBasePage):
    """
    My Courses List screen
    """

    def get_my_courses_list(self):
        """
        Get My Courses List

        Returns:
            webdriver element: My Courses List Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_courses_list
        )

    def get_my_courses_list_row(self):
        """
        Get My Course row

        Returns:
            webdriver element: My Course row Element
        """

        courses_row = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.my_courses_list_course_row
        )

        if courses_row:
            return courses_row[0]
        else:
            return courses_row

    def get_my_course_name(self):
        """
        Get Course name

        Returns:
            webdriver element: My Course name Element
        """

        course_name = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.my_courses_list_course_row
        )

        return course_name[0] if course_name[0] else course_name[0]

    def get_my_course_details(self):
        """
        Get Course details

        Returns:
            webdriver element: My Course details Element
        """

        my_course_details = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.my_courses_list_course_details
        )

        return my_course_details[0] if my_course_details[0] else my_course_details[0]

    def get_find_courses_message(self):
        """
        Get Course Message

        Returns:
            webdriver element: Courses Message Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_courses_list_find_courses_message
        )

    def get_find_course_button(self):
        """
        Get Find Course

        Returns:
            webdriver element: Find Course button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_courses_list_find_course_button
        )

    def load_course_details_screen(self):
        """
        Load Course Details

        Returns:
            webdriver element: Find Course button element
        """

        self.get_my_course_name().click()
        self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_details_last_accessed_textview
        )
        course_details = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return course_details[0] if course_details[0] else course_details[0]

    def load_discovery_screen(self):
        """
        Load Discovery Screen

        Returns:
            webdriver element: Discovery screen title element
        """

        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        horizontal_start_point = int((screen_width * 40) / 100)
        vertical_start_point = int((screen_height * 80) / 100)
        horizontal_end_point = horizontal_start_point
        vertical_end_point = int((screen_width * 10) / 100)

        self.log.info('Screen width {} -screen height {} - horizontal_start_point {} - vertical_start_point {} '
                      '- horizontal_end_point {} '
                      '- vertical_end_point {}'.format(screen_width, screen_height, horizontal_start_point,
                                                       vertical_start_point, horizontal_end_point, vertical_end_point
                                                       ))
        self.driver.swipe(horizontal_start_point, vertical_start_point, horizontal_end_point, vertical_end_point, 500)

        # self.get_find_course_button().click()

        output = self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.course_discovery_textview
        )
        if output:
            return self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.course_discovery_textview
            )
        else:
            self.global_contents.wait_for_element_visibility(
                self.driver,
                ios_elements.course_discovery_textview
            )

            return self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.course_discovery_textview
            )
