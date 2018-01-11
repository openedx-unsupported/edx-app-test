"""
    Main Dashboard Test Module
"""
from pages.whats_new import WhatsNew
from pages.main_dashboard import MainDashboard
from testdata.input_data import InputData
from common.globals import Globals
from common.strings import Strings


class TestMainDashborad():
    """
    Main Dashborad screen's Test Case
    """
    @staticmethod
    def test_start_main_dashboard_smoke(login, set_capabilities):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        print('-- Starting ', TestMainDashborad.__name__, 'Test Case')

        if login:
            print(InputData.login_user_name, 'is successfully logged in')

        whats_new_page = WhatsNew(set_capabilities)
        if InputData.target_environment == Strings.ANDROID:
            assert whats_new_page.exit_features() == Globals.VIEW_MY_COURSES_ACTIVITY_NAME

        elif InputData.target_environment == Strings.IOS:
            assert whats_new_page.exit_features().text == Strings.MAIN_DASHBOARD_SCREEN_TITLE

    @staticmethod
    def test_validate_ui_elements(set_capabilities):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                     Screen Title, Menu Drawer, Account Menu option and Log out user
                Verify all screen contents have their default values
                Verify that user can log out successfully, and back on Login screen
        """

        main_dashborad_page = MainDashboard(set_capabilities)

        textview_screen_title = main_dashborad_page.get_title_textview()
        assert textview_screen_title is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_screen_title.text == Strings.MAIN_DASHBOARD_SCREEN_TITLE

        image_button_drawer = main_dashborad_page.get_drawer_icon()
        assert image_button_drawer is not None
        if InputData.target_environment == Strings.IOS:
            assert image_button_drawer.text == Strings.MAIN_DASHBOARD_NAV_MENU

        textview_drawer_account_option = main_dashborad_page.get_drawer_account_option()
        assert textview_drawer_account_option is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_drawer_account_option.text == Strings.MAIN_DASHBOARD_NAV_ACCOUNT_OPTION

        textview_screen_title = main_dashborad_page.log_out()
        assert textview_screen_title is not None
        if InputData.target_environment == Strings.ANDROID:
            assert textview_screen_title == Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        elif InputData.target_environment == Strings.IOS:
            assert textview_screen_title.text == Strings.LOGIN_SCREEN_TITLE
        print('-- Ending ', TestMainDashborad.__name__, 'Test Case')
