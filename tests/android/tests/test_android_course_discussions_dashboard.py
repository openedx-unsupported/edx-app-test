"""
    Course Discussions Dashboard Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_discussions_dashboard import AndroidCourseDiscussionsDashboard
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages import android_elements


class TestAndroidCourseDiscussionsDashboard(AndroidLoginSmoke):
    """
    Course Discussions Dashboard screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that Course Dashboard tab will show following contents,
        Header contents,
            Back icon,
            Specific "<course name>" as Title, Share icon, Course,
        Verify that user should be able to go back by clicking Back icon
        Verify that user should be able to view these Course contents:
            Course Image, Course Name, Course Provider, Course Ending date,
            Last accessed(if any), Course Content,
        Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        discussions_dashboard_page = AndroidCourseDiscussionsDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_first_course().text
            android_my_courses_list_page.get_first_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert android_course_dashboard_page.get_navigation_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_NAVIGATION_ICON

        discussion_tab_element = android_course_dashboard_page.get_discussion_tab()
        if discussion_tab_element:
            discussion_tab_element.click()
            assert discussion_tab_element.get_attribute('selected') == 'true'

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discussion_search_post).text == strings.DISCUSSION_SEARCH_POST

        assert global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence).text == strings.DISCUSSION_ALL_POSTS

        assert global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.second_existence).text == strings.DISCUSSION_MY_FOLLOWING_POSTS

        assert global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.third_existence).text == strings.DISCUSSION_GENERAL_POSTS

        global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence).click()

        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS
        discussions_dashboard_page.get_navigation_icon().click()

        global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.second_existence).click()

        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_MY_FOLLOWING_POSTS
        discussions_dashboard_page.get_navigation_icon().click()

        global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.third_existence).click()

        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_GENERAL_POSTS
        discussions_dashboard_page.get_navigation_icon().click()

        set_capabilities.back()
        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case --')
