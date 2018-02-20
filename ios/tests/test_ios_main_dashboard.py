"""
    Main Dashboard Test Module
"""
from common import strings
from common.globals import Globals
from input_data import InputData
from ios.pages.ios_main_dashboard import IosMainDashboard
from ios.pages.ios_whats_new import IosWhatsNew


class TestIosMainDashboard():
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        log = setup_logging
        global_contents = Globals(log)

        log.info('-- Starting {} Test Case'.format(TestIosMainDashboard.__name__))
        if login:
            log.info('{} is successfully logged in'.format(InputData.login_user_name))

        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        if global_contents.is_first_time:
            assert ios_whats_new_page.exit_features().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        else:
            assert ios_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                     Screen Title, Menu Drawer, Account Menu option and Log out user
                Verify all screen contents have their default values
                Verify that user can log out successfully, and back on Login screen
        """

        log = setup_logging
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        # Commenting it temporarily, it should be fix with LEARNER-3888
        # textview_screen_title = ios_main_dashboard_page.get_title_textview()
        # assert textview_screen_title.text == strings.MAIN_DASHBOARD_SCREEN_TITLE

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU
        assert ios_main_dashboard_page.get_drawer_account_option().text == strings.MAIN_DASHBOARD_NAVIGATION_ACCOUNT_OPTION
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN_IOS_WITH_EMAIL_DIVIDER

        log.info('-- Ending {} Test Case'.format(TestIosMainDashboard.__name__))
