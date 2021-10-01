"""
    Course Discussions Dashboard Page Module
"""
from selenium.webdriver.common.keys import Keys

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosDiscussionsDashboard(IosBasePage):
    """
    Course Discussionns Dashboard screen
    """

    def get_share_icon(self):
        """
        Get share icon

        Returns:
            webdriver element: Share icon Element
        """

        share_icon_element = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dahsboard_share_icon
        )

        return share_icon_element

    def get_subsection_title(self):
        """
        Wait for all textview on screen
        Returns:
            webdriver element: Subsection title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.all_textviews
        )

        all_textviews_on_screen = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return all_textviews_on_screen[0]

    def get_navigation_icon(self):
        """
        Wait for navigation icon
        Returns:
            webdriver element: Navigation icon
        """

        navigation_icon = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[self.global_contents.first_existence]

        return navigation_icon

    def get_posts_search_element(self):
        """
        wait for posts search row
        Returns:
            webdriver element: Posts search element
        """

        posts_search_element = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.discussions_dashboard_search_post
        )[0]

        return posts_search_element

    def search_post(self):
        """
        Get search post element
        search post by a keyword
        """

        post_search_row = self.get_posts_search_element()

        post_search_row.click()
        post_search_row.send_keys('General')
        post_search_row.send_keys(Keys.ENTER)
