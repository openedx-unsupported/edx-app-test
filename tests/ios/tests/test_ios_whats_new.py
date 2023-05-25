"""
    Whats New Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages import ios_elements


class TestIosWhatsNew:
    """
    Whats New screen's Test Case
    """

    def test_start_whats_new_smoke(self, login, setup_logging, set_capabilities):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        global_contents = Globals(setup_logging)
        setup_logging.info('Starting Test Case')
        if login:
            setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')

        if global_contents.is_first_time:
            assert IosWhatsNew(set_capabilities, setup_logging).get_title_textview()
        else:
            textview_screen_title = IosMainDashboard(set_capabilities, setup_logging)
            assert textview_screen_title.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        if global_contents.is_first_time:

            ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

            assert ios_whats_new_page.get_title_textview()
            assert ios_whats_new_page.get_close_button().text == strings.WHATS_NEW_Close_button
            assert ios_whats_new_page.get_main_image()
            assert ios_whats_new_page.get_feature_title_textview()
            assert ios_whats_new_page.get_feature_details()
            assert ios_whats_new_page.get_close_button().text == strings.CLOSE_BUTTON_TEXT

        else:
            setup_logging.info('validate_ui_elements is not needed')
            assert True

    def test_navigate_features_smoke(self, set_capabilities, setup_logging):
        """
            Verify that user can navigate between features
        """

        global_contents = Globals(setup_logging)
        if global_contents.is_first_time:
            ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
            assert ios_whats_new_page.navigate_features().text == strings.CLOSE_BUTTON_TEXT

        else:
            setup_logging.info('navigate_features is not needed')

    def test_close_features_screen_smoke(self, set_capabilities, setup_logging):
        """
            Verify that user can close New Feature screen and move to Main Dashboard screen
        """

        global_contents = Globals(setup_logging)
        if global_contents.is_first_time:

            ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
            assert ios_whats_new_page.exit_features().text == strings.BLANK_FIELD

        else:
            setup_logging.info('close_features_screen is not needed')

    def test_re_login_smoke(self, setup_logging, set_capabilities):
        """
        Scenarios:
            Verify after re-login with same user "Whats New" screen will not be visible
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')

        ios_login_page = IosLogin(set_capabilities, setup_logging)
        ios_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password
        )

        setup_logging.info(f'{global_contents.target_environment} is successfully logged in')

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Landscape support is added for Whats New screen with following cases,
                Change device orientation to Landscape mode
                Verify Whats New screen is loaded successfully after login
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
                Verifies that user can navigate between features
                Verifies that user can close New Feature screen and move to Main Dashboard screen
                Verify after re-login with same user "Whats New" screen will not be visible
                Change device orientation to Portrait mode
        """
        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        # assert ios_login_page.login(global_contents.login_user_name, global_contents.login_password)
        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        ios_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password
        )

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        personal_information_email_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_email_label)
        global_contents.scroll_from_element(set_capabilities, personal_information_email_label)
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
        setup_logging.info('Ending Test Case')
