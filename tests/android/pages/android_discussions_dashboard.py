"""
    Course Discussions Dashboard Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidDiscussionsDashboard(AndroidBasePage):
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

    def get_screen_title(self):
        """"
        Returns:
            "Webdriver elements: First element of text_views"

        """

        return self.get_all_text_views()[0]

    def search_post(self, driver):
        """
        Get search post element
        search post by a keyword
        """

        post_search_row = self.global_contents.get_element_by_id(
            driver,
            android_elements.discussion_search_post)

        post_search_row.click()
        post_search_row.send_keys('General')
        self.driver.press_keycode(self.global_contents.android_enter_key)
