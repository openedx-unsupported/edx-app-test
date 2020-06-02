# coding=utf-8

"""
    My Courses List Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


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
            android_elements.my_courses_list_find_course_button,
            1
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
            self.global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        )

    def scroll_course_list_and_click_find_course_button(self):
        """
        Scroll through all courses unless 'Find a Course' button is not available
        """

        course_names_list = []
        course_details_list = []
        course_title_details = []

        while True:
            course_list_last_element = self.get_course_list()[-1]
            course_names = self.get_all_course_names()
            course_details = self.get_all_course_details()
            for names, details in zip(course_names, course_details):
                if names.text not in course_names_list and details.text not in course_details_list:
                    course_names_list.append(names.text)
                    course_details_list.append(details.text)

            if self.get_find_course_button():
                break

            self.global_contents.scroll_from_element(self.driver, course_list_last_element)

        count = len(course_details_list)
        for i in range(count - 1):
            course_title_details.append([course_names_list[i], course_details_list[i]])

    def get_course_list(self):
        """
        Get Course List

        Returns:
            list of courses
        """

        course_list = self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.main_dashboard_course_list
        )
        return course_list

    def get_all_course_names(self):
        """
        Get Courses List Name

        Returns:
            Courses List Name
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.main_dashboard_course_name
        )

    def get_all_course_details(self):
        """
        Get Courses Details

        Returns:
            Courses Details List
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.main_dashboard_course_details
        )
