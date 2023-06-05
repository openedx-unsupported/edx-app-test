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
                    Screen Title, Learn Tab
                    Profile Tab, Discover Tab
            Verify that Learn tab will be selected by default
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        assert android_main_dashboard_page.get_my_courses_dropdown().text == strings.MAIN_DASHBOARD_MY_COURSES_DROPDOWN
        learn_tab = android_main_dashboard_page.get_all_tabs()[1]
        assert learn_tab.text == 'Learn'
        assert learn_tab.get_attribute('selected') == 'true'

        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        assert discover_tab.text == 'Discover'
        assert discover_tab.get_attribute('selected') == 'false'

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        assert profile_tab.get_attribute('selected') == 'false'

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify on tapping Discover will load Discover screen
                Verify on tapping Profile will load Profile screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        discover_tab.click()
        assert discover_tab.get_attribute('selected') == 'true'
        assert android_main_dashboard_page.get_screen_heading().get_attribute('content-desc') \
            == strings.MAIN_DASHBOARD_DISCOVER_SCREEN_HEADING

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        profile_tab.click()
        assert profile_tab.get_attribute('selected') == 'true'
        assert android_main_dashboard_page.get_screen_heading().get_attribute('content-desc') \
            == strings.MAIN_DASHBOARD_PROFILE

    def test_logout_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that user can log out successfully, and back on Login screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')

        setup_logging.info(f'Ending {TestAndroidMainDashboard.__name__} Test Case')

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Landscape support is added for Main Dashboard screen with following cases,
                Verify following contents are visible on screen, 
                    Screen Title, Learn Tab
                    Profile Tab, Discover Tab
                Verify that Learn tab will be selected by default
                Verify on tapping Discover will load Discover screen
                Verify on tapping Profile will load Profile screen
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

        assert android_main_dashboard_page.get_all_text_views()[0].text == strings.MAIN_DASHBOARD_MY_COURSES_DROPDOWN
        learn_tab = android_main_dashboard_page.get_all_tabs()[1]
        assert learn_tab.text == 'Learn'
        assert learn_tab.get_attribute('selected') == 'true'

        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        assert discover_tab.text == 'Discover'
        assert discover_tab.get_attribute('selected') == 'false'
        discover_tab.click()
        assert discover_tab.get_attribute('selected') == 'true'
        assert android_main_dashboard_page.get_screen_heading().get_attribute('content-desc') \
            == strings.MAIN_DASHBOARD_DISCOVER_SCREEN_HEADING

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        assert profile_tab.get_attribute('selected') == 'false'
        profile_tab.click()
        assert profile_tab.get_attribute('selected') == 'true'
        assert android_main_dashboard_page.get_screen_heading().get_attribute('content-desc') \
            == strings.MAIN_DASHBOARD_PROFILE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify tapping Account Icon will load Account Screen
            Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
            Verify that user can logout from main dashboard screen
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')

        setup_logging.info(f'Ending {TestAndroidMainDashboard.__name__} Test Case')
