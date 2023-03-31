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

        course_dahsboard_share_icon = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dahsboard_share_icon
        )
        return course_dahsboard_share_icon

    def get_course_image(self):
        """
        Get course image

        Returns:
            webdriver element: course image Element
        """

        course_dashboard_course_image = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_image
        )
        return course_dashboard_course_image

    def get_course_title(self):
        """
        Get course title

        Returns:
            webdriver element: course title Element
        """

        course_dashboard_course_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_title
        )
        return course_dashboard_course_title

    def get_course_date(self):
        """
        Get course date

        Returns:
            webdriver element: course date Element
        """

        course_dashboard_course_date = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_date
        )
        return course_dashboard_course_date

    def get_course_section_header(self):
        """
        Get course section header

        Returns:
            webdriver element: course section header Element
        """

        course_section_header = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_section_header
        )
        return course_section_header

    def get_course_item_title(self):
        """
        Get course item title

        Returns:
            webdriver element: course item title Element
        """

        course_item_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_item_title
        )
        return course_item_title

    def get_course_item_download_icon(self):
        """
        Get course item download icon

        Returns:
            webdriver element: course item download icon Element
        """

        course_item_download = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_course_item_download
        )
        return course_item_download

    def get_courses_tab(self):
        """
        Get course tab

        Returns:
            webdriver element: course tab Element
        """

        courses_tab = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_courses_tab
        )
        return courses_tab

    def get_videos_tab(self):
        """
        Get videos tab

        Returns:
            webdriver element: videos tab Element
        """

        videos_tab = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_videos_tab
        )
        return videos_tab

    def get_discussion_tab(self):
        """
        Get discussion tab

        Returns:
            webdriver element: discussion tab Element
        """

        discussion_tab = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_discussion_tab
        )
        return discussion_tab

    def get_dates_tab(self):
        """
        Get dates tab

        Returns:
            webdriver element: dates tab Element
        """

        dates_tab = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_dates_tab
        )
        return dates_tab

    def get_resources_tab(self):
        """
        Get resources tab

        Returns:
            webdriver element: resources tab Element
        """

        resources_tab = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_resources_tab
        )
        return resources_tab

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

        resources_list_title = self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_title
        )[0]
        return resources_list_title

    def get_handouts_row_name(self):
        """
        Get handouts row name

        Returns:
            webdriver element: handouts row name Element
        """

        resources_list_name = self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_name
        )
        return resources_list_name[0]

    def get_announcements_row_title(self):
        """
        Get announcements row title

        Returns:
            webdriver element: announcements row title Element
        """

        resources_list_title = self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_title
        )
        return resources_list_title[1]

    def get_announcements_row_name(self):
        """
        Get announcements row name

        Returns:
            webdriver element: announcements row name Element
        """

        resources_list_name = self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.course_dashboard_resources_list_name
        )
        return resources_list_name[1]

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

    def get_course_resume_row(self):
        """
        Load course dashboard screen

        Returns:
            webdriver element: course resume Element
        """

        resume_row = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_resume_row
        )
        return resume_row

    def get_resources_back_icon(self):
        """
        Load course dashboard screen

        Returns:
            webdriver element: course resume Element
        """

        resources_back_icon = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_resources_back_icon
        )
        return resources_back_icon

    def navigate_to_main_dashboard(self, set_capabilities):
        """
        Get navigation icon and navigate to main dashboard screen to logout

        """

        set_capabilities.back()
        set_capabilities.back()
        set_capabilities.back()
        set_capabilities.back()

    def get_my_courses_list_row(self):
        """
        Get My Course row

        Returns:
            webdriver element: My Course row Element
        """

        courses_row = self.global_contents.get_all_elements_by_id(
            self.driver,
            ios_elements.my_courses_list_course_row
        )
        return courses_row[0]

    def load_course_details_screen(self):
        """
        Load Course Details

        Returns:
            webdriver element: Find Course button element
        """

        self.get_my_courses_list_row().click()
        self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_details_last_accessed_textview
        )
        course_details = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )
        return course_details[1]
