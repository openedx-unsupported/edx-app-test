"""
    Whats New Test Module
"""
from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidWhatsNews:
    """
    Whats New screen's Test Case
    """

    def test_start_whats_new_smoke(self, setup_logging, set_capabilities, login):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        setup_logging.info('-- Starting Test Case')

        if login:
            android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
            assert android_whats_new_page.on_screen() == Globals.WHATS_NEW_ACTIVITY_NAME
        else:
            android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
            assert android_main_dashboard_page.on_screen() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging, login):
        """
        Scenarios:
                Verify following contents are visible on screen 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        if login:
            android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

            assert android_whats_new_page.get_title_textview()
            assert android_whats_new_page.get_cross_icon()
            assert android_whats_new_page.get_main_image().text == strings.BLANK_FIELD
            assert android_whats_new_page.get_feature_title_textview()
            assert android_whats_new_page.get_feature_details()

        else:
            setup_logging.info('validate_ui_elements is not needed')

    def test_navigate_features_smoke(self, set_capabilities, setup_logging, login):
        """
        Verifies that user can navigate between features
        """

        if login:
            android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
            android_whats_new_page.navigate_features()
            assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE

        else:
            setup_logging.info('navigate_features is not needed')

    def test_close_features_screen_smoke(self, set_capabilities, setup_logging, login):
        """
        Verifies that user can close New Feature screen and move to Main Dashboard screen
        """

        if login:
            android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
            assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        else:
            setup_logging.info('close_features is not needed')

    def test_re_login_smoke(self, setup_logging, set_capabilities):
        """
        Scenarios:
            Verify after re-login with same user "Whats New" screen will not be visible
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == global_contents.NEW_LOGISTRATION_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')

        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)

        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        login_output = android_login_page.login(global_contents.login_user_name, global_contents.login_password, False)

        assert login_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.target_environment} is successfully logged in')

        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == global_contents.NEW_LOGISTRATION_ACTIVITY_NAME

        setup_logging.info('-- Ending Test Case')
