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

    def test_navigate_to_all_posts_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that user can navigate to Discussion Dashboard
        Verify that on Discussion dashboard All Posts option can be clickable
        Verify that All posts screen will show following contents in header:
            Navigation icon,
            All posts as Title,
        Verify that on clicking navigation icon user move to dashboard screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_second_course_row().text
            assert ios_my_courses_list.load_second_course_detail_screen().text in course_name

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

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that All posts screen will show following contents,
        Refine label
        All posts filter
        Recent activity filter
        Create new post
        Verify that clicking create new post will open its page
        """

        global_contents = Globals(setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        all_posts_element = global_contents.get_by_class_from_elements(
            set_capabilities,
            ios_elements.discussions_topic_title_cell,
            global_contents.first_existence
        )
        all_posts_element.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_ALL_POSTS

        refine_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_posts_refine_text_view)
        assert refine_label.text == strings.COURSE_ALL_POSTS_REFINE_LABEL

        all_posts = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_all_posts_option)
        assert all_posts.text == strings.COURSE_ALL_POSTS_LABEL_IOS

        recent_activity = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_recent_activity_option)
        assert recent_activity.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY_IOS

    def test_all_post_filter_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that All post filter can be clickable
            Verify All posts, Unread, Unanswered can be visibile in filter popup
            Verify all filter can be clickable
        """

        global_contents = Globals(setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        all_posts = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_all_posts_option)
        all_posts.click()

        unread_filter = ios_discussions_page.get_all_buttons()[2]
        assert unread_filter.text == strings.COURSE_ALL_POSTS_UNREAD

        unanswered_posts = ios_discussions_page.get_all_buttons()[3]
        assert unanswered_posts.text == strings.COURSE_ALL_POSTS_UNANSWERED

        cancel_button = ios_discussions_page.get_all_buttons()[4]
        assert cancel_button.text == strings.COURSE_ALL_POSTS_CANCEL_BUTTON

        unread_filter.click()
        unread_posts = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_all_posts_option)
        assert unread_posts.text == strings.COURSE_ALL_POSTS_UNREAD_IOS

        unread_posts.click()
        unanswered_filter = ios_discussions_page.get_all_buttons()[3]
        assert unanswered_filter.text == strings.COURSE_ALL_POSTS_UNANSWERED
        unanswered_filter.click()
        unanswered_posts = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_all_posts_option)
        assert unanswered_posts.text == strings.COURSE_ALL_POSTS_UNANSWERED_IOS

    def test_recent_activity_filter_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that recent activity can be clickable
            Verify recent activity, most activity, most votes can be visibile in filter popup
            Verify all filter can be clickable
        """

        global_contents = Globals(setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        recent_activity = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_recent_activity_option)
        assert recent_activity.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY_IOS
        recent_activity.click()
        most_activity_filter = ios_discussions_page.get_all_buttons()[2]
        assert most_activity_filter.text == strings.COURSE_ALL_POSTS_MOST_ACTIVITY

        most_votes_filter = ios_discussions_page.get_all_buttons()[3]
        assert most_votes_filter.text == strings.COURSE_ALL_POSTS_MOST_VOTES

        most_activity_filter.click()
        most_activity_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_recent_activity_option)
        assert most_activity_label.text == strings.COURSE_ALL_POSTS_MOST_ACTIVITY_IOS
        most_activity_label.click()

        most_votes_filter = ios_discussions_page.get_all_buttons()[3]
        assert most_votes_filter.text == strings.COURSE_ALL_POSTS_MOST_VOTES
        most_votes_filter.click()
        most_votes_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.discussion_recent_activity_option)
        assert most_votes_label.text == strings.COURSE_ALL_POSTS_MOST_VOTES_IOS

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
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        setup_logging.info('Ending Test Case')
