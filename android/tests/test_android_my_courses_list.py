# coding=utf-8

"""
    My Courses List Test Module
"""
from android.pages.android_login import AndroidLogin
from android.pages.android_main_dashboard import AndroidMainDashboard
from android.pages.android_my_courses_list import AndroidMyCoursesList
from android.pages.android_new_landing import AndroidNewLanding
from android.pages.android_whats_new import AndroidWhatsNew
from common import strings
from common.globals import Globals


class TestAndroidMyCoursesList(object):
    """
    My Courses List's Test Case
    """

    def test_start_my_courses_list_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
                list(of specific logged in user) in its tab
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidMyCoursesList.__name__))

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
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        assert android_whats_new_page.navigate_features()
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        assert android_main_dashboard_page.load_courses_tab()

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard  tapping Courses tab will load My Courses contents(of specific logged in user) in its tab
            Verify that Courses tab/screen will show following header contents,,
            Header Contents
                Profile icon
                "Courses" title
                Account Icon
            Courses Tab
            Discovery Tab
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidMyCoursesList.__name__))
