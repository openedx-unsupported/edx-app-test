# coding=utf-8

"""
    My Courses List Module
"""
from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage


class AndroidMyCoursesList(AndroidBasePage):
    """
    My Courses List screen
    """

    def get_my_courses_list(self):
        """
        Get Courses List

        Returns:
            webdriver element: Courses List Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_list
        )

    def get_my_courses_list_row(self):
        """
        Get My Course row

        Returns:
            webdriver element: My Course row Element
        """

        courses_row = self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.my_courses_list_course_row
        )

        if courses_row:
            return courses_row[self.global_contents.first_existence]
        else:
            return courses_row

    def get_find_courses_message(self):
        """
        Get Course Message

        Returns:
            webdriver element: Courses Message Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_list_find_courses_message
        )

    def get_find_course_button(self):
        """
        Get Find Course

        Returns:
            webdriver element: Find Course button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_list_find_course_button
        )

    def get_contents_from_list(self):
        """
        Get Course Contents
        """

        course_rows = self.global_contents.get_elements_from_list(
            self.driver,
            android_elements.my_courses_list,
            android_elements.my_courses_list_course_row
        )

        self.global_contents.get_elements_from_list(
            self.driver,
            android_elements.my_courses_list,
            android_elements.my_courses_list_course_name
        )

        self.global_contents.get_elements_from_list(
            self.driver,
            android_elements.my_courses_list,
            android_elements.my_courses_list_course_details
        )

        self.log.info('Total {} course rows are visible on screen. '.format(len(course_rows)))

    def load_course_details_screen(self):
        """
        Tap on some course to load its details screen

        Returns:
            str: Course Details Activity Name
        """

        self.global_contents.get_elements_from_list(
            self.driver,
            android_elements.my_courses_list,
            android_elements.my_courses_list_course_name
        )[0].click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
        )

    def load_discovery_screen(self):
        """
        Tap on Find a Course button to load Course Discovery screen

        Returns:
            str: Course Discovery Activity Name
        """

        self.get_find_course_button().click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.WEB_VIEW_FIND_COURSES_ACTIVITY_NAME
        )
