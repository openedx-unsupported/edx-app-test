"""
    Main Dashboard Test Module
"""
from input_data import InputData
from common.globals import Globals
from common import strings
from ios.pages.ios_whats_new import IosWhatsNew
from ios.pages.ios_main_dashboard import IosMainDashboard

class TestIosMainDashborad():
    """
    Main Dashborad screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        log = setup_logging
        global_contents = Globals(log)

        log.info('-- Starting {} Test Case'.format(TestIosMainDashborad.__name__))

        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        ios_main_dashborad_page = IosMainDashboard(set_capabilities, setup_logging)

<<<<<<< HEAD
        if global_contents.IsFirstTime:
=======
        if global_contents.is_first_time:
>>>>>>> c721227... Merged Test Automation restructure part
            assert ios_whats_new_page.exit_features().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        else:
            assert ios_main_dashborad_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                     Screen Title, Menu Drawer, Account Menu option and Log out user
                Verify all screen contents have their default values
                Verify that user can log out successfully, and back on Login screen
        """

        log = setup_logging
        ios_main_dashborad_page = IosMainDashboard(set_capabilities, setup_logging)

        textview_screen_title = ios_main_dashborad_page.get_title_textview()
        assert textview_screen_title is not None
        assert textview_screen_title.text == strings.MAIN_DASHBOARD_SCREEN_TITLE

        image_button_drawer = ios_main_dashborad_page.get_drawer_icon()
        assert image_button_drawer is not None
        assert image_button_drawer.text == strings.MAIN_DASHBOARD_NAV_MENU

        textview_drawer_account_option = ios_main_dashborad_page.get_drawer_account_option()
        assert textview_drawer_account_option is not None
        assert textview_drawer_account_option.text == strings.MAIN_DASHBOARD_NAV_ACCOUNT_OPTION

        textview_screen_title = ios_main_dashborad_page.log_out()
        assert textview_screen_title is not None

        assert textview_screen_title.text == strings.LOGIN_SCREEN_TITLE

        log.info('-- Ending {} Test Case'.format(TestIosMainDashborad.__name__))
