"""
    Course Discussions Dashboard Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_discussions_dashboard import IosDiscussionsDashboard
from tests.ios.pages.ios_login_smoke import IosLoginSmoke
from tests.ios.pages import ios_elements


class TestIosDiscussionsDashboard(IosLoginSmoke):
    """
    Course Discussions Dashboard screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from My Courses list tapping any Course will load Course
                Dashboard screen/contents(of this specific course) in its tab
            Verify on tapping "Videos" tab will load Videos screen
            Verify on tapping "Discussion" tab will load Discussions screen
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
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_courses_list_row().text
            assert ios_my_courses_list.load_course_details_screen().text in course_name

        assert ios_course_dashboard_page.get_courses_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_videos_tab().text == strings.COURSE_DASHBOARD_VIDEOS_TAB
        ios_course_dashboard_page.load_videos_tab()
        assert ios_course_dashboard_page.get_videos_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_discussion_tab().text == strings.COURSE_DASHBOARD_DISCUSSION_TAB
        ios_course_dashboard_page.load_discussion_tab()
        assert ios_course_dashboard_page.get_discussion_tab().text == global_contents.is_selected

        assert ios_discussions_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_DASHBOARD_TITLE
        assert ios_discussions_page.get_navigation_icon().text == 'Courses'
        assert ios_discussions_page.get_posts_search_element().text == strings.DISCUSSION_SEARCH_POST

        all_posts_element = global_contents.get_by_class_from_elements(
            set_capabilities,
            ios_elements.discussions_topic_title_cell,
            global_contents.first_existence
            )
        assert all_posts_element.text == strings.DISCUSSION_ALL_POSTS

        following_posts_element = global_contents.get_by_class_from_elements(
            set_capabilities,
            ios_elements.discussions_topic_title_cell,
            global_contents.second_existence
            )
        assert following_posts_element.text == " Posts I'm Following"

        course_feedback_element = global_contents.get_by_class_from_elements(
            set_capabilities,
            ios_elements.discussions_topic_title_cell,
            global_contents.third_existence
            )
        assert course_feedback_element.text == strings.DISCUSSION_COURSE_QnA

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping All Posts will load its screen
            Verify on tapping Posts i'm following will load its screen
            Verify on tapping General will load its screen
            Verify on searching any post in search bar will load results screen
        """

        global_contents = Globals(setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        ios_discussions_page.search_post()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_SEARCH_RESULTS
        ios_discussions_page.get_navigation_icon().click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_DASHBOARD_TITLE

        all_posts_element = global_contents.get_by_class_from_elements(
            set_capabilities,
            ios_elements.discussions_topic_title_cell,
            global_contents.first_existence
            )
        all_posts_element.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_ALL_POSTS
        ios_discussions_page.get_navigation_icon().click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_DASHBOARD_TITLE

        following_posts_element = global_contents.get_by_class_from_elements(
            set_capabilities,
            ios_elements.discussions_topic_title_cell,
            global_contents.second_existence
            )
        following_posts_element.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_MY_FOLLOWING_POSTS_IOS
        ios_discussions_page.get_navigation_icon().click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_DASHBOARD_TITLE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course discussions screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page.navigate_to_main_dashboard(set_capabilities)
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info(' Ending Test Case --')
