"""
    Course Discussion Details Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_discussions_dashboard import AndroidDiscussionsDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages import android_elements


class TestAndroidDiscussionDetails(AndroidLoginSmoke):
    """
    Course Discussions Details screen's Test Case

    """

    def test_navigate_to_discussion_screen(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that user can navigate to Discussion dashboard page after login
        Verify that user can click on Discussion tab
        Verify that user can click on all posts element
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.get_second_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        navigation_icon = android_course_dashboard_page.get_navigation_icon()
        assert navigation_icon.get_attribute('content-desc') == strings.COURSE_DASHBOARD_NAVIGATION_ICON

        discussion_tab_element = android_course_dashboard_page.get_discussion_tab()
        discussion_tab_element.click()
        assert discussion_tab_element.get_attribute('selected') == strings.TRUE

        all_posts_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.discussion_all_posts_button,
            global_contents.first_existence)
        all_posts_element.click()

        # my_following_posts_element = global_contents.get_by_id_from_elements(
        #     set_capabilities,
        #     android_elements.discussion_all_posts_button,
        #     global_contents.second_existence)
        # my_following_posts_element.click()
        # assert discussions_dashboard_page.get_screen_title().text == strings.DISCUSSION_MY_FOLLOWING_POSTS
        # discussions_dashboard_page.get_navigation_icon().click()

    def test_create_new_post_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify user can click on create new item
        Verify the title of page
        Verify that user can fill title and body of post discussion form
        Verify user can click on post discussion button
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
        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        first_post = global_contents.get_all_elements_by_id(
            set_capabilities,
            android_elements.discussion_following_post)
        assert first_post[0].text == strings.DISCUSSION_DETAILS_TEST_RESPONSE
        first_post[0].click()
        assert discussions_dashboard_page.get_screen_title().text == strings.CREATE_POST_DISCUSSION_BUTTON

        profile_image = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_profile_image
        )
        assert profile_image.get_attribute('displayed') == strings.TRUE

        author_text = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion__author_text_view
        )
        assert author_text.get_attribute('displayed') == strings.TRUE
        assert author_text.text == 'AutomationTester'

        number_responses = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_number_responses
        )
        assert number_responses.get_attribute('displayed') == strings.TRUE
        assert number_responses.text == strings.DISCUSSION_DETAILS_RESPONSES_TEXT

        date_text_view = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_date_text_view
        )
        assert date_text_view.get_attribute('displayed') == strings.TRUE
        assert date_text_view.text

        thread_row_title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_responses_thread_row_title
        )
        assert thread_row_title.get_attribute('displayed') == strings.TRUE
        assert thread_row_title.text

        thread_row_body = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_responses_thread_row_body
        )
        assert thread_row_body.get_attribute('displayed') == strings.TRUE
        assert thread_row_body.text

        thread_row_visibility = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_responses_thread_row_visibility
        )
        assert thread_row_visibility.get_attribute('displayed') == strings.TRUE
        assert thread_row_visibility.text == strings.DISCUSSION_DETAILS_POST_VISIBILITY_TEXT

        add_response = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_create_new_item
        )
        assert add_response.get_attribute('displayed') == strings.TRUE
        assert add_response.text == strings.DISCUSSION_DETAILS_ADD_COMMENT_TEXT
        add_response.click()

    def test_add_resopnse_page_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that following elements should be visible on Add response page
        Author text
        Date text
        Title text row
        Body text row
        """

        global_contents = Globals(setup_logging)

        author_text = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion__author_text_view
        )
        assert author_text.get_attribute('displayed') == strings.TRUE
        assert author_text.text == 'AutomationTester'

        date_text_view = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discssion_date_text_view
        )
        assert date_text_view.get_attribute('displayed') == strings.TRUE
        assert date_text_view.text

        thread_row_title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.disussion_add_comment_row_title
        )
        assert thread_row_title.get_attribute('displayed') == strings.TRUE
        assert thread_row_title.text

        thread_row_body = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.disussion_add_comment_row_body
        )
        assert thread_row_body.get_attribute('displayed') == strings.TRUE
        assert thread_row_body.text

    def test_add_new_comment_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify user can click on add comment button
        Verify that user can add a comment in field
        Verify that user can click on add response button
        Verify that user can see banner of your response has been added
        """

        global_contents = Globals(setup_logging)
        add_new_comment = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discussion_add_new_comment
        )
        assert add_new_comment.get_attribute('displayed') == strings.TRUE
        assert add_new_comment.text == strings.DISCUSSION_DETAILS_ADD_COMMENT_TEXT
        add_new_comment.click()
        add_new_comment.send_keys('Automated test comment')
        add_response = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discussion_add_new_comment_button
        )
        assert add_response.get_attribute('displayed') == strings.TRUE
        assert add_response.text == strings.DISCUSSION_DETAILS_ADD_RESPONSE_TEXT
        add_response.click()
        flying_message = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.discussion_flying_message
        )
        assert flying_message.text == strings.DISCUSSION_DETAILS_FLYING_MESSAGE_TEXT
        assert flying_message.get_attribute('displayed') == strings.TRUE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course discussions details screen
        """

        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        discussions_dashboard_page.get_navigation_icon().click()
        discussions_dashboard_page.get_navigation_icon().click()
        discussions_dashboard_page.get_navigation_icon().click()
        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case --')
