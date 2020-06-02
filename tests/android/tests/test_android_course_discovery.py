# coding=utf-8

"""
    My Courses List Test Module
"""

from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_course_discovery import AndroidCourseDiscovery
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseDiscovery:
    """
    Discovery Test Case
    """

    def test_discovery_screen(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping on Discovery tab will load Discovery
            contents in its tab
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidCourseDiscovery.__name__))

        global_contents = Globals(setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_new_landing_page.on_screen() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        assert android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password,
            global_contents.is_first_time
        ) == Globals.WHATS_NEW_ACTIVITY_NAME

        android_whats_new_page.navigate_features()
        assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        # android_whats_new_page.navigate_features()
        # assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        assert android_main_dashboard_page.load_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.load_discovery_tab().is_selected()

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
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
