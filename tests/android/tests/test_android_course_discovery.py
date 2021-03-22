# coding=utf-8

"""
    My Courses List Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_course_discovery import AndroidCourseDiscovery
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseDiscovery(AndroidLoginSmoke):
    """
    Discovery Test Case
    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that from Main Dashboard tapping on Discovery tab will load Discovery
            contents in its tab
        Verify that Discovery tab will show following contents,
        Header contents,
            Profile icon, "Discovery" as screen Title,
            Discovery edit-field in place title(Android Only), Account Icon
        Three tabs
            Courses, Programs, Degrees
        "Browse By Subject" Section below, Subject Background Image, Subject Name
        "Viewing <total number of available results"
        Filter courses option
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_course_discovery_page = AndroidCourseDiscovery(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.load_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.load_discovery_tab().is_selected()
        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.COURSES_DISCOVERY_SCREEN_TITLE
        assert android_course_discovery_page.get_search_icon().text == strings.BLANK_FIELD
        search_editfield = android_course_discovery_page.load_search_editfield().text
        assert search_editfield == strings.COURSES_DISCOVERY_SEARCH_EDIT_FIELD
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        browse_by_subject_heading = android_course_discovery_page.get_browse_by_subject_heading().text
        assert browse_by_subject_heading == strings.COURSES_DISCOVERY_BROWSE_BY_SUBJECT_LABEL
        assert android_course_discovery_page.get_subject_name().text == strings.COURSES_DISCOVERY_SUBJECT_NAME
        assert android_course_discovery_page.get_subject_image().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
