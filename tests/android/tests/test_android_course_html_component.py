"""
    Course HTMl component Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_subsection import AndroidCourseSubsection
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_course_html_component import AndroidCourseHTMLComponent
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

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_course_section_page = AndroidCourseSubsection(set_capabilities, setup_logging)
        course_html_component = AndroidCourseHTMLComponent(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.load_course_details_screen()
        else:
            setup_logging.info('No course enrolled by this user.')

        topic_name = android_course_section_page.get_course_row_header().text
        android_course_section_page.get_course_row_header().click()

        if topic_name:
            assert android_course_dashboard_page.get_all_text_views()[0].text in topic_name

        course_topic_content = android_course_section_page.get_course_topic_row().text

        android_course_section_page.get_course_topic_row().click()
        assert android_course_dashboard_page.get_all_text_views()[0].text in course_topic_content

        assert course_html_component.get_next_button().text == strings.COURSE_HTML_COMPONENT_NEXT_BUTTON
        assert course_html_component.get_prev_button().text == strings.COURSE_HTML_COMPONENT_PREV_BUTTON
        assert course_html_component.get_next_unit_title()
        course_html_component.get_next_button().click()
        assert course_html_component.get_screen_activity_name() == global_contents.COURSE_UNIT_NAVIGATION_ACTIVITY_NAME
        assert course_html_component.get_prev_unit_title()
        course_html_component.get_prev_button().click()
        assert android_course_dashboard_page.get_all_text_views()[0].text in course_topic_content
