"""
    Course Discussions All Posts Test Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_discussions_dashboard import \
    AndroidDiscussionsDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseAllPosts(AndroidLoginSmoke):
    """
    Course Discussions All Posts screen's Test Case

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
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.get_first_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        navigation_icon = android_course_dashboard_page.get_navigation_icon()
        assert navigation_icon.get_attribute('content-desc') == strings.COURSE_DASHBOARD_NAVIGATION_ICON

        discussion_tab_element = android_course_dashboard_page.get_discussion_tab()
        discussion_tab_element.click()
        assert discussion_tab_element.get_attribute('selected') == 'true'

        all_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence)
        assert all_posts_element.text == strings.DISCUSSION_ALL_POSTS
        all_posts_element.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS
        discussions_dashboard_page.get_navigation_icon().click()

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
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        all_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence)
        all_posts_element.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS
        post_refine_label = discussions_dashboard_page.get_all_text_views()[1]
        assert post_refine_label.text == strings.COURSE_ALL_POSTS_REFINE_LABEL

        course_all_post_label = discussions_dashboard_page.get_all_text_views()[2]
        assert course_all_post_label.text == strings.COURSE_ALL_POSTS_LABEL

        recent_activity_post = discussions_dashboard_page.get_all_text_views()[3]
        assert recent_activity_post.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY

        post_refine_label = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discussion_posts_refine_text_view)
        assert post_refine_label.text == strings.COURSE_ALL_POSTS_REFINE_LABEL

        create_new_item_text_view = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_new_item_text_view)
        assert create_new_item_text_view.text == strings.COURSE_ALL_POSTS_CREATE_NEW_POST
        create_new_item_text_view.click()

        create_post_page_title = discussions_dashboard_page.get_all_text_views()[0]
        assert create_post_page_title.text == strings.COURSE_ALL_POSTS_CREATE_NEW_POST

        navigation_icon = discussions_dashboard_page.get_navigation_icon()
        assert navigation_icon.get_attribute('content-desc') == strings.COURSE_DASHBOARD_NAVIGATION_ICON
        navigation_icon.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS

    def test_all_post_filter_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that All post filter can be clickable
            Verify All posts, Unread, Unanswered can be visibile in filter popup
            Verify all filter can be clickable
        """

        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        discussions_dashboard_page.get_all_text_views()[2].click()

        course_all_post_label = discussions_dashboard_page.get_all_text_views()[0]
        assert course_all_post_label.text == strings.COURSE_ALL_POSTS_LABEL

        all_post_unread = discussions_dashboard_page.get_all_text_views()[1]
        assert all_post_unread.text == strings.COURSE_ALL_POSTS_UNREAD

        all_post_unanswered = discussions_dashboard_page.get_all_text_views()[2]
        assert all_post_unanswered.text == strings.COURSE_ALL_POSTS_UNANSWERED

        discussions_dashboard_page.get_all_text_views()[0].click()

        course_all_post_label = discussions_dashboard_page.get_all_text_views()[2]
        assert course_all_post_label.text == strings.COURSE_ALL_POSTS_LABEL
        course_all_post_label.click()

        all_post_unread = discussions_dashboard_page.get_all_text_views()[1]
        assert all_post_unread.text == strings.COURSE_ALL_POSTS_UNREAD
        all_post_unread.click()

        unread_posts = discussions_dashboard_page.get_all_text_views()[2]
        assert unread_posts.text == strings.COURSE_ALL_POSTS_UNREAD
        unread_posts.click()

        post_unanswered = discussions_dashboard_page.get_all_text_views()[2]
        assert post_unanswered.text == strings.COURSE_ALL_POSTS_UNANSWERED
        post_unanswered.click()

        unanswered_posts_header = discussions_dashboard_page.get_all_text_views()[2]
        assert unanswered_posts_header.text == strings.COURSE_ALL_POSTS_UNANSWERED

    def test_recent_activity_filter_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that recent activity can be clickable
            Verify recent activity, most activity, most votes can be visibile in filter popup
            Verify all filter can be clickable
        """

        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        recent_activity_label = discussions_dashboard_page.get_all_text_views()[3]
        assert recent_activity_label.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY
        recent_activity_label.click()

        recent_activity_filter = discussions_dashboard_page.get_all_text_views()[0]
        assert recent_activity_filter.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY

        most_activity_filter = discussions_dashboard_page.get_all_text_views()[1]
        assert most_activity_filter.text == strings.COURSE_ALL_POSTS_MOST_ACTIVITY

        most_votes_filter = discussions_dashboard_page.get_all_text_views()[2]
        assert most_votes_filter.text == strings.COURSE_ALL_POSTS_MOST_VOTES
        most_activity_filter.click()

        most_activity_label = discussions_dashboard_page.get_all_text_views()[3]
        assert most_activity_label.text == strings.COURSE_ALL_POSTS_MOST_ACTIVITY
        most_activity_label.click()

        most_votes_filter = discussions_dashboard_page.get_all_text_views()[2]
        assert most_votes_filter.text == strings.COURSE_ALL_POSTS_MOST_VOTES
        most_votes_filter.click()

        most_votes_label = discussions_dashboard_page.get_all_text_views()[3]
        assert most_votes_label.text == strings.COURSE_ALL_POSTS_MOST_VOTES
        most_votes_label.click()

        recent_activity_filter = discussions_dashboard_page.get_all_text_views()[0]
        assert recent_activity_filter.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY
        recent_activity_filter.click()
        recent_activity_label = discussions_dashboard_page.get_all_text_views()[3]
        assert recent_activity_label.text == strings.COURSE_ALL_POSTS_RECENT_ACTIVITY

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course discussions screen
        """

        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        discussions_dashboard_page.get_navigation_icon().click()
        discussions_dashboard_page.get_navigation_icon().click()
        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case')
