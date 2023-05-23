"""
    Main Dashboard Test Module
"""
from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidMainDashboard(AndroidLoginSmoke):
    """
    Main Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
         Scenarios:
                Verify following contents are visible on screen, 
                    Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_all_text_views()[0].text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify on tapping Courses will load Courses contents in its tab
                Verify on tapping Programs will load Programs contents in its tab
                Verify on tapping Discovery will load Discovery contents in its tab
                Verify tapping Menu Icon will load Profile Options Screen
                Verify tapping back/cancel icon from Profile Options Screen should get back to Main Dashboard screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.get_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB
        assert android_main_dashboard_page.load_programs_tab().is_selected()
        assert android_main_dashboard_page.load_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.load_discovery_tab().is_selected()
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.load_courses_tab().is_selected()

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        set_capabilities.back()

    def test_logout_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that user can log out successfully, and back on Login screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')

        setup_logging.info(f'-- Ending {TestAndroidMainDashboard.__name__} Test Case')

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
                Verify on tapping Programs will load Programs contents in its tab
                Verify on tapping Discovery will load Discovery contents in its tab
                Verify tapping user's avatar will load User Profile screen
                Verify tapping back/cancel icon from User Profile screen should get back to Main Dashboard screen
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_new_landing_page.on_screen() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        login_output = android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password, False)
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')
        assert login_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        assert android_main_dashboard_page.get_all_text_views()[0].text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        assert android_main_dashboard_page.load_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB
        assert android_main_dashboard_page.load_programs_tab().is_selected()
        assert android_main_dashboard_page.load_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.load_discovery_tab().is_selected()
        assert android_main_dashboard_page.load_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.load_courses_tab().is_selected()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify tapping Account Icon will load Account Screen
            Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
            Verify that user can logout from main dashboard screen
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        set_capabilities.back()

        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)

        setup_logging.info(f'-- Ending {TestAndroidMainDashboard.__name__} Test Case')
