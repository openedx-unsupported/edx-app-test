# coding=utf-8
"""
    Main Dashboard Test Module
"""
from android.pages.android_main_dashboard import AndroidMainDashboard
from android.pages.android_whats_new import AndroidWhatsNew
from common.globals import Globals
from common import strings


class TestAndroidMainDashboard(object):
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        global_contents = Globals(setup_logging)
        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidMainDashboard.__name__))
        if login:
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_whats_new_page.navigate_features()
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
         Scenarios:
                Verify following contents are visible on screen, 
                    Logged in user's avatar, Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify on tapping Courses will load Courses contents in its tab
                Verify on tapping Discovery will load Discovery contents in its tab
                Verify tapping user's avatar will load User Profile screen
                Verify tapping back/cancel icon from User Profile screen should get back to Main Dashboard screen
                Verify tapping Account Icon will load Account Screen
                Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.load_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB

        assert android_main_dashboard_page.load_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        assert android_main_dashboard_page.load_profile_screen() == global_contents.PROFILE_ACTIVITY_NAME
        set_capabilities.back()

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        set_capabilities.back()

    def test_logout_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that user can log out successfully, and back on Login screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))

        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidMainDashboard.__name__))
