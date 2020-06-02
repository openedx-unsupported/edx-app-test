# coding=utf-8
"""
    Main Dashboard Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew


class TestIosMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        global_contents = Globals(setup_logging)

        setup_logging.info('-- Starting Test Case')
        if login:
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        if global_contents.is_first_time:
            assert ios_whats_new_page.exit_features().text == strings.BLANK_FIELD
        else:
            assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    Logged in user's avatar, Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.load_profile_screen().text == strings.PROFILE_SCREEN_TITLE
        ios_main_dashboard_page.get_close_button().click()
        # set_capabilities.back()
        assert ios_main_dashboard_page.get_title_textview_portrait_mode().text == strings.BLANK_FIELD
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.get_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

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

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.load_discovery_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB

        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        assert ios_main_dashboard_page.load_profile_screen().text == strings.PROFILE_SCREEN_TITLE
        ios_main_dashboard_page.get_close_button().click()
        # set_capabilities.back()

        assert ios_main_dashboard_page.load_account_screen().text == strings.ACCOUNT_SCREEN_TITLE
        ios_main_dashboard_page.get_close_button().click()
        # set_capabilities.back()

    def test_logout_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that user can log out successfully, and back on Login screen
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert ios_main_dashboard_page.get_account_options()[3].text == strings.ACCOUNT_LOGOUT
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Landscape support is added for Main Dashboard screen with following cases,
                Change device orientation to Landscape mode
                Verify following contents are visible on screen, 
                    Logged in user's avatar, Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
                Verify on tapping Courses will load Courses contents in its tab
                Verify on tapping Discovery will load Discovery contents in its tab
                Verify tapping user's avatar will load User Profile screen
                Verify tapping back/cancel icon from User Profile screen should get back to Main Dashboard screen
                Verify tapping Account Icon will load Account Screen
                Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
                Verify that user can log out successfully, and back on Login screen
        """

        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        assert ios_login_page.login(global_contents.login_user_name, global_contents.login_password, False)
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        assert ios_main_dashboard_page.get_profile_icon().text == strings.MAIN_DASHBOARD_PROFILE
        assert ios_main_dashboard_page.get_title_textview_landscape_mode().text == strings.BLANK_FIELD
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.get_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        assert ios_main_dashboard_page.load_discovery_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert ios_main_dashboard_page.load_profile_screen().text == strings.PROFILE_SCREEN_TITLE
        ios_main_dashboard_page.get_close_button().click()
        # set_capabilities.back()
        assert ios_main_dashboard_page.load_account_screen().text == strings.ACCOUNT_SCREEN_TITLE
        ios_main_dashboard_page.get_close_button().click()
        # set_capabilities.back()

        assert ios_main_dashboard_page.get_account_options()[3].text == strings.ACCOUNT_LOGOUT
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)

        setup_logging.info('-- Ending Test Case')
