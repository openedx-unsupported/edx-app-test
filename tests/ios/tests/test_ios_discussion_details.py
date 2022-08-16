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


class TestIosDiscussionDetails(IosLoginSmoke):
    """
    Course Discussions Details screen's Test Case

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
        all_posts_element.click()

    def test_create_new_post_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify user can click on create new item
        Verify the title of page
        Verify that user can fill title and body of post discussion form
        Verify user can click on post discussion button
        """

        global_contents = Globals(setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)

        create_new_post_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_new_post_button
        )
        assert create_new_post_button.text == strings.CREATE_NEW_POST_BUTTON_IOS
        create_new_post_button.click()
        create_post_title = ios_discussions_page.get_all_text_views()[1]
        assert create_post_title.text == strings.COURSE_ALL_POSTS_CREATE_NEW_POST

        discussion_button = ios_discussions_page.get_all_buttons()[7]
        discussion_button.click()
        assert discussion_button.get_attribute('label') == strings.CREATE_POST_DISCUSSION_BUTTON_IOS
        title_field = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.create_post_title_edit_text_field)
        assert title_field.text == strings.CREATE_POSTS_EDIT_TITLE_TEXT
        title_field.click()
        title_field.send_keys('Automated test discussion')

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

    def test_discussion_details_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify user should navigated to Discussion Details screen
        Verify these element on discussion details screen
        Profile image
        Author text
        Number Responses
        Date text
        Title text row
        Body text row
        Visibility text row
        Add response button
        Verify user can click on Add response button
        """

        global_contents = Globals(setup_logging)

        first_post_title = global_contents.get_all_elements_by_id(
            set_capabilities,
            ios_elements.discussion_post_title_label
        )[1]
        assert first_post_title.text == strings.DISCUSSION_DETAILS_TEST_RESPONSE
        first_post_title.click()

        author_text = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discssion__author_text_view)
        assert author_text.get_attribute('visible') == strings.TRUE
        assert author_text.text == 'AutomationTester'

        number_responses = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discssion_number_responses)
        assert number_responses.text == strings.DISCUSSION_DETAILS_RESPONSES_TEXT_IOS

        title_label = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discssion_responses_thread_row_title)
        assert title_label.text == strings.DISCUSSION_DETAILS_TEST_RESPONSE

        body_label = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discssion_responses_thread_row_body)
        assert body_label.text == strings.DISCUSSION_DETAILS_TEST_RESPONSE

        visibility_row = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discssion_responses_thread_row_visibility)
        assert visibility_row.text == strings.DISCUSSION_DETAILS_POST_VISIBILITY_TEXT

        vote_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discussion_details_vote_button)
        assert vote_button.text == strings.DISCUSSION_DETAILS_VOTE_BUTTON_IOS

        unfollow_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discussion_details_unfollow_button)
        assert unfollow_button.text == strings.DISCUSSION_DETAILS_UNFOLLOW_BUTTON

        report_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discussion_details_report_button)
        assert report_button.text == strings.DISCUSSION_DETAILS_REPORT_BUTTON

        add_response_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discussion_details_add_response_button)
        assert add_response_button.text == strings.DISCUSSION_DETAILS_ADD_COMMENT_TEXT_IOS
        add_response_button.click()

    def test_add_resopnse_page_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify user can click on add comment button
        Verify that user can add a comment in field
        Verify that user can click on add response button
        Verify that user can see banner of your response has been added
        """

        global_contents = Globals(setup_logging)

        add_new_response = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discussion_details_add_new_response)
        add_new_response.click()
        add_new_response.send_keys('automated response')
        add_new_response_button = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_buttons
        )[7]
        assert add_new_response_button.text == strings.DISCUSSION_DETAILS_ADD_RESPONSE_TEXT
        add_new_response_button.click()
        status_message = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.discussion_details_status_message
        )
        assert status_message.text == strings.DISCUSSION_DETAILS_FLYING_MESSAGE_TEXT

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
