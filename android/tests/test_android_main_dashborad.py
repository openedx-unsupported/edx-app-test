"""
    Main Dashboard Test Module
"""
from android.pages.android_main_dashboard import AndroidMainDashboard
from android.pages.android_whats_new import AndroidWhatsNew
from common.globals import Globals
from input_data import InputData


class TestAndroidMainDashboard():
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """
        log = setup_logging

        log.info('-- Starting {} Test Case'.format(TestAndroidMainDashboard.__name__))
        if login:
            log.info('{} is successfully logged in'.format(InputData.login_user_name))

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        assert android_whats_new_page.exit_features() == Globals.VIEW_MY_COURSES_ACTIVITY_NAME

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                     Screen Title, Menu Drawer, Account Menu option and Log out user
                Verify all screen contents have their default values
                Verify that user can log out successfully, and back on Login screen
        """
        log = setup_logging
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_title_textview()
        assert android_main_dashboard_page.get_drawer_icon()
        assert android_main_dashboard_page.get_drawer_account_option()
        assert android_main_dashboard_page.log_out() == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        log.info('-- Ending {} Test Case'.format(TestAndroidMainDashboard.__name__))
