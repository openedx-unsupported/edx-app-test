"""
    Course Create New Posts Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_discussions_dashboard import AndroidDiscussionsDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages import android_elements


class TestAndroidCreateNewPost(AndroidLoginSmoke):
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
        all_posts_element.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that from All posts screen user can click on create new post,
        Verify on clicking user should navigate to create new post screen
        Verify that create new post screen has following elements:
        Navigation icon
        Create new post as header
        Verify that clicking navigation icon will navigate to all post screen
        Verify that clicking create new post will open its page
        """

        global_contents = Globals(setup_logging)
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
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

        create_new_item_text_view = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_new_item_text_view)
        create_new_item_text_view.click()

    def test_create_discussion_post(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that create new post show discussion button checked by Default
        Verify that text of discussion button
        Verify that topic spinner is visible on screen
        Verify that Title and body should have text
        Verify that user can post a discussion by submitting form
        Verify on clicking post discussion user should navigate to all post screen
        """

        global_contents = Globals(setup_logging)
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        discussion_button = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_discussion_button)
        assert discussion_button.text == strings.CREATE_POST_DISCUSSION_BUTTON
        assert discussion_button.get_attribute('checked') == 'true'

        topic_spinner = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_topics_spinner)
        assert topic_spinner

        title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_title_edit_text)
        assert title.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT
        title.click()
        title.send_keys('Automated test discussion')

        post_body = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_body_edit_text)
        assert post_body.text == strings.CREATE_POST_DISCUSSION_BUTTON
        post_body.click()
        post_body.send_keys('Automated test discussion')

        post_discussion = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_add_post_button)
        assert post_discussion.text == strings.CREATE_POSTS_ADD_DISCUSSION_POST
        post_discussion.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS

        create_new_item_text_view = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_new_item_text_view)
        create_new_item_text_view.click()
        create_post_page_title = discussions_dashboard_page.get_all_text_views()[0]
        assert create_post_page_title.text == strings.COURSE_ALL_POSTS_CREATE_NEW_POST

    def test_create_question_post(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that create new post show question button not selected by Default
        Verify that text of question button
        Verify that topic spinner is visible on screen
        Verify that Title and body should have text
        Verify that user can post a question by submitting form
        Verify on clicking post question user should navigate to all post screen
        """

        global_contents = Globals(setup_logging)
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        question_button = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_question_button)
        assert question_button.text == strings.CREATE_POST_QUESTION_BUTTON
        assert question_button.get_attribute('checked') == 'false'
        question_button.click()
        assert question_button.get_attribute('checked') == 'true'

        title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_title_edit_text)
        assert title.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT
        title.click()
        title.send_keys('Automated test question')

        post_body = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_body_edit_text)
        assert post_body.text == strings.CREATE_POST_QUESTION_BUTTON
        post_body.click()
        post_body.send_keys('Automated test question')

        post_discussion = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.create_post_add_post_button)
        assert post_discussion.text == strings.CREATE_POST_ADD_QUESTION_TEXT
        post_discussion.click()
        assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_ALL_POSTS

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
        setup_logging.info('Ending Test Case --')
