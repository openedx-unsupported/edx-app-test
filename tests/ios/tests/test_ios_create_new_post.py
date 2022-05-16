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


class TestIosCreateNewPost(IosLoginSmoke):
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
        all_posts_element.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_ALL_POSTS

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
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        create_new_post_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_new_post_button
            )
        assert create_new_post_button.text == strings.COURSE_ALL_POSTS_CREATE_NEW_POST
        create_new_post_button.click()
        create_post_title = ios_discussions_page.get_all_text_views()[1]
        assert create_post_title.text == strings.COURSE_ALL_POSTS_CREATE_NEW_POST

        cancel_button = ios_discussions_page.get_all_buttons()[1]
        assert cancel_button.text == strings.CANCEL_BUTTON
        cancel_button.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_ALL_POSTS
        create_new_post_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_new_post_button)
        create_new_post_button.click()

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
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        question_button = ios_discussions_page.get_all_buttons()[6]
        assert question_button.get_attribute('label') == strings.CREATE_POST_QUESTION_BUTTON_IOS

        topic_spinner = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_topics_spinner)
        assert topic_spinner.get_attribute('label') == strings.CREATE_POST_TOPIC_SPINNER_TEXT

        title = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_title_edit_text)
        assert title.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT_IOS

        title_field = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_title_edit_text_field)
        assert title_field.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT
        title_field.click()
        title_field.send_keys('Automated test question')

        question_label = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_question_label)
        assert question_label.text == strings.CREATE_POST_QUESTION_LABEL_IOS

        question_field = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_question_text_field)
        assert question_field.text == strings.CREATE_POST_QUESTION_BUTTON
        question_field.click()
        question_field.send_keys('Automated test question')

        post_question = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_add_post_button)
        assert post_question.text == strings.CREATE_POST_ADD_QUESTION_TEXT
        post_question.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_ALL_POSTS

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
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        create_new_post_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_new_post_button)
        create_new_post_button.click()
        discussion_button = ios_discussions_page.get_all_buttons()[7]
        discussion_button.click()
        assert discussion_button.get_attribute('label') == strings.CREATE_POST_DISCUSSION_BUTTON_IOS

        topic_spinner = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_topics_spinner)
        assert topic_spinner.get_attribute('label') == 'Topic: Course Q&A'

        title = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_title_edit_text)
        assert title.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT_IOS

        title_field = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_title_edit_text_field)
        assert title_field.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT
        title_field.click()
        title_field.send_keys('Automated test discussion')

        question_label = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_question_label)
        assert question_label.text == strings.CREATE_POST_DISCUSSION_LABEL_IOS

        question_field = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_question_text_field)
        assert question_field.text == strings.CREATE_POST_DISCUSSION_BUTTON
        question_field.click()
        question_field.send_keys('Automated test discussion')

        post_discussion = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_add_post_button)
        assert post_discussion.text == strings.CREATE_POSTS_ADD_DISCUSSION_POST
        post_discussion.click()
        assert ios_discussions_page.get_subsection_title().text == strings.DISCUSSION_ALL_POSTS

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
