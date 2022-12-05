"""
    Main Dashboard Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosMainDashboard(IosLoginSmoke):
    """
    Main Dashboard screen's Test Case
    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    Logged in user's avatar, Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_title_textview_portrait_mode().get_attribute('label') \
            == strings.MAIN_DASHBOARD_COURSES_TAB
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.get_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.DISCOVER_COURSES_SCREEN_TITLE

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
        assert ios_main_dashboard_page.get_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB

        assert ios_main_dashboard_page.load_programs_tab().text == strings.SELECTED_BY_DEFAULT

        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.DISCOVER_COURSES_SCREEN_TITLE

        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        ios_main_dashboard_page.get_acccount_close_button().click()

    def test_logout_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that user can log out successfully, and back on Login screen
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
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
        """

        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        assert ios_login_page.login(global_contents.login_user_name, global_contents.login_password)
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        assert ios_main_dashboard_page.get_title_textview_landscape_mode().text == strings.BLANK_FIELD
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.get_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.DISCOVER_COURSES_SCREEN_TITLE

        assert ios_main_dashboard_page.load_discovery_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert ios_main_dashboard_page.load_programs_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.DISCOVER_COURSES_SCREEN_TITLE
        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify tapping Account Icon will load Account Screen
                Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
                Verify that user can log out successfully, and back on Login screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        personal_information_email_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_email_label)
        global_contents.scroll_from_element(set_capabilities, personal_information_email_label)
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
        setup_logging.info('-- Ending Test Case')
