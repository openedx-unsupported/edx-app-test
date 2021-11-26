"""
    Course Subsection Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_subsection import AndroidCourseSubsection
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseSubsection(AndroidLoginSmoke):
    """
    Course Subsection screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Course Topics screen will show following Header contents:
                Back icon
                Specific "<Topic name>" as Title
            Verify that user should be able to go back by clicking Back icon
            Verify that user should be able to view these on Every Topic in the list:
                Topic name
                Topic icon
            download icon to video (if available)
            Verify that on Clicking any topic Specific resource screen should be loaded successfully
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_course_section_page = AndroidCourseSubsection(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.load_course_details_screen()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert android_course_section_page.get_course_row_title()

        topic_name = android_course_section_page.get_course_row_title().text
        android_course_section_page.get_course_row_title().click()
        assert android_course_dashboard_page.get_navigation_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_NAVIGATION_ICON
        android_course_dashboard_page.get_navigation_icon().click()
        assert android_course_section_page.on_screen() == global_contents.COURSE_DASHBOARD_ACTIVITY_NAME

        android_course_section_page.get_course_row_title().click()
        if topic_name:
            # Verifing the title of the screen
            assert android_course_dashboard_page.get_all_text_views()[0].text in topic_name

        assert android_course_dashboard_page.get_course_content_header()
        assert android_course_section_page.get_course_topic_row().text == strings.COURSE_SUBSECTION_CONTENT_ROW_TEXT
        assert android_course_section_page.get_course_video_row().text == strings.COURSE_SUBSECTION_VIDEO_ROW_TEXT
        assert android_course_section_page.get_topic_download_icon()

        course_topic_content = android_course_section_page.get_course_row_title().text

        android_course_section_page.get_course_row_title().click()
        assert android_course_dashboard_page.get_all_text_views()[0].text in course_topic_content
        set_capabilities.back()

        course_video_content = android_course_section_page.get_course_video_row().text
        android_course_section_page.get_course_video_row().click()
        assert android_course_dashboard_page.get_all_text_views()[0].text in course_video_content

        android_course_section_page.navigate_to_main_dashboard(set_capabilities)
        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('-- Ending Test Case --')
