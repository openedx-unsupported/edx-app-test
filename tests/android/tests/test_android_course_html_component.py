"""
    Course HTMl component Test Module
"""

from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_html_component import \
    AndroidCourseHTMLComponent
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseHTMLComponent(AndroidLoginSmoke):
    """
    Course HTML component screen's Test Case

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

        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        course_html_component = AndroidCourseHTMLComponent(set_capabilities, setup_logging)

        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_second_course().text
            android_my_courses_list_page.get_second_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        if course_name:
            # Verifing the title of the screen
            assert course_name in android_course_dashboard_page.course_dashboard_course_title().text

        assert android_course_dashboard_page.get_course_section_row_title().text
        assert android_course_dashboard_page.get_course_sub_section_row_title().text
        subsection_name = android_course_dashboard_page.get_course_sub_section_row_title().text
        assert subsection_name == strings.COURSE_SUBSECTION_TITLE

        android_course_dashboard_page.get_course_sub_section_row_title().click()
        assert android_course_dashboard_page.get_course_sub_section_screen_title().text in subsection_name

        assert course_html_component.get_next_button().text == strings.COURSE_HTML_COMPONENT_NEXT_BUTTON
        assert course_html_component.get_prev_button().text == strings.COURSE_HTML_COMPONENT_PREV_BUTTON
        course_html_component.get_next_button().click()
        course_html_component.get_prev_button().click()
        assert android_course_dashboard_page.get_course_sub_section_screen_title().text in subsection_name

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course html screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        set_capabilities.back()
        set_capabilities.back()
        assert android_main_dashboard_page.get_profile_tab().text == strings.PROFILE_SCREEN_TITLE
        android_main_dashboard_page.get_profile_tab().click()

        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case')
