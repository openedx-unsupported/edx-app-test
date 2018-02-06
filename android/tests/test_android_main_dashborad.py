"""
    Main Dashboard Test Module
"""
from input_data import InputData
from common.globals import Globals
from android.pages.android_whats_new import AndroidWhatsNew
from android.pages.android_main_dashboard import AndroidMainDashboard


class TestAndroidMainDashborad():
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

        log.info('-- Starting {} Test Case'.format(TestAndroidMainDashborad.__name__))
        if login:
            log.info('{} is successfully logged in'.format(InputData.login_user_name))

        andriod_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        assert andriod_whats_new_page.exit_features() == Globals.VIEW_MY_COURSES_ACTIVITY_NAME

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                     Screen Title, Menu Drawer, Account Menu option and Log out user
                Verify all screen contents have their default values
                Verify that user can log out successfully, and back on Login screen
        """
        log = setup_logging
        andriod_main_dashborad_page = AndroidMainDashboard(set_capabilities, setup_logging)

        textview_screen_title = andriod_main_dashborad_page.get_title_textview()
        assert textview_screen_title is not None

        image_button_drawer = andriod_main_dashborad_page.get_drawer_icon()
        assert image_button_drawer is not None

        textview_drawer_account_option = andriod_main_dashborad_page.get_drawer_account_option()
        assert textview_drawer_account_option is not None

        textview_screen_title = andriod_main_dashborad_page.log_out()
        assert textview_screen_title is not None

        assert textview_screen_title == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        log.info('-- Ending {} Test Case'.format(TestAndroidMainDashborad.__name__))
