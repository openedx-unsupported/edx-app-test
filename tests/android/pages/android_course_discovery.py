"""
    Discovery Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidCourseDiscovery(AndroidBasePage):
    """
    My Discovery screen
    """

    def get_search_icon(self):
        """
        Find Search icon

        Returns:
            webdriver element: Search Icon
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_search_icon
        )

    def load_search_editfield(self):
        """
        Load Search Edit Field

        Returns:
            webdriver element: Search editfiled
        """

        self.get_search_icon().click()
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_search_editfield
        )

    def get_courses_tab(self):
        """
        Find courses tab

        Returns:
            webdriver element: Courses Tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_courses_tab
        )

    def get_programs_tab(self):
        """
        Find programs tab

        Returns:
            webdriver element: Programs Tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_programs_tab
        )

    def get_find_degrees_tab(self):
        """
        Find degrees tab

        Returns:
            webdriver element: Degrees Tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_degrees_tab
        )

    def get_browse_by_subject_heading(self):
        """
        Find Browse by Subject Heading

        Returns:
            webdriver element: Browse By Subject
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_browse_by_subject_label
        )

    def get_subject_name(self):
        """
        Find Subject Name

        Returns:
            webdriver element: Subject Name
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_subject_name
        )

    def get_subject_image(self):
        """
        Find Subject Image

        Returns:
            webdriver element: Subject Imange
        """

        self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews)

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.coruses_discovery_subject_background_image
        )
