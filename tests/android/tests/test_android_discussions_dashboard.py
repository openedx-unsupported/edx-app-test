"""
    Course Discussions Dashboard Test Module
"""

from appium.webdriver.common.mobileby import MobileBy
from tests.android.pages import android_elements
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_discussions_dashboard import \
    AndroidDiscussionsDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidDiscussionsDashboard(AndroidLoginSmoke):
    """
    Course Discussions Dashboard screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that Course Discussions Dashboard tab will show following contents,
        Header contents,
            Back icon,
            Discussions as Title,
        Verify that user should be able to view these Course contents:
            Search posts,
            All posts,
            Posts I'm following,
            General
        Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)

        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.get_first_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().get_attribute(
            'clickable') == strings.TRUE

        assert android_course_dashboard_page.course_dashboard_course_organization().text \
            == strings.LOGIN_EDX_LOGO
        assert android_course_dashboard_page.course_dashboard_course_expiry_date().text

        scrollable_tab = set_capabilities.find_element(MobileBy.ID, android_elements.course_dashboard_tabs)
        tab_elements = scrollable_tab.find_elements(MobileBy.CLASS_NAME, android_elements.course_layout)

        discussion_tab = tab_elements[2]
        assert discussion_tab.get_attribute('selected') == strings.FALSE
        discussion_tab.click()
        assert discussion_tab.get_attribute('selected') == strings.TRUE

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discussion_search_post).text == strings.DISCUSSION_SEARCH_POST

        all_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence)
        assert all_posts_element.text == strings.DISCUSSION_ALL_POSTS

        my_following_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.second_existence)
        assert my_following_posts_element.text == strings.DISCUSSION_MY_FOLLOWING_POSTS

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping All Posts will load its screen
            Verify on tapping Posts i'm following will load its screen
            Verify on tapping General will load its screen
            Verify on searching any post in search bar will load results screen
        """

        global_contents = Globals(setup_logging)
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)

        all_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence)
        all_posts_element.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS
        discussions_dashboard_page.get_navigation_icon().click()

        my_following_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.second_existence)
        my_following_posts_element.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_MY_FOLLOWING_POSTS
        discussions_dashboard_page.get_navigation_icon().click()

        discussions_dashboard_page.search_post(set_capabilities)
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_SEARCH_RESULTS

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course discussions screen
        """

        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        discussions_dashboard_page.get_navigation_icon().click()
        set_capabilities.back()
        set_capabilities.back()
        assert android_main_dashboard_page.get_profile_tab().text == strings.PROFILE_SCREEN_TITLE
        android_main_dashboard_page.get_profile_tab().click()

        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case')
