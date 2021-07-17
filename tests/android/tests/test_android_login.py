"""
    Login Test Module
"""

import pytest

from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages.android_whats_new import AndroidWhatsNew


class TestAndroidLogin:
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Login screen is loaded successfully
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidLogin.__name__))

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        assert android_login_page.on_screen() == Globals.LOGIN_ACTIVITY_NAME

        setup_logging.info('Login screen successfully loaded')

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_login_page.get_title_textview().text == strings.LOGIN
        assert android_login_page.get_logo().get_attribute('content-desc') == strings.EDX_LOGO
        assert android_login_page.get_username_editfield().text == strings.LOGIN_USER_NAME_WATER_MARK_ANDROID
        assert android_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK
        assert android_login_page.get_forgot_password_textview().text == strings.LOGIN_FORGOT_PASSWORD
        assert android_login_page.get_sign_in_button().text == strings.LOGIN
        login_with_email_divider = android_login_page.get_login_with_email_divider_textview().text
        assert login_with_email_divider == strings.LOGIN_ANDROID_WITH_EMAIL_DIVIDER
        assert android_login_page.get_facebook_textview().text == strings.FACEBOOK_OPTION
        assert android_login_page.get_google_textview().text == strings.GOOGLE_OPTION
        assert android_login_page.get_agreement_textview().text == strings.LOGIN_ANDROID_AGREEMENT

    @pytest.mark.skip(reason="No id could be assigned to part of string, will figure it out later")
    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping back icon from 'Sign In' screen navigate user
                    back to 'New Landing' screen.
                Verify that user is able to load EULA screen and get back to Login Screen
                Verify that user is able to load Terms screen and get back to Login Screen
                Verify that user is able to load Privacy screen and get back to Login Screen
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_login_page.back_and_forth_login()
        assert android_login_page.load_eula_screen()
        assert android_login_page.load_terms_screen()
        assert android_login_page.load_privacy_screen()

    def test_forgot_password_alert(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping 'Forgot your password?' will  load 'Reset Password' alert
                Verify following contents are visible on 'Reset Password' alert, 
                Alert Title, Alert Message, Email edit field, Cancel & OK buttons
                Verify tapping 'Cancel' will close 'Reset Password' alert
                Verify tapping 'Ok' will show make email field requied and
                    show email format alert message.
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_login_page.get_forgot_password_alert()

        assert android_login_page.get_forgot_password_alert_title().text == strings.LOGIN_RESET_PASSWORD_ALERT_TITLE
        get_forgot_password_alert_msg = android_login_page.get_forgot_password_alert_msg().text
        assert get_forgot_password_alert_msg == strings.LOGIN_RESET_PASSWORD_ALERT_MSG_ANDROID
        assert android_login_page.get_forgot_password_alert_ok_button().text == strings.LOGIN_RESET_PASSWORD_ALERT_OK
        forgot_password_alert_cancel_button = android_login_page.get_forgot_password_alert_cancel_button().text
        assert forgot_password_alert_cancel_button == strings.LOGIN_RESET_PASSWORD_ALERT_CANCEL_ANDROID
        android_login_page.get_forgot_password_alert_ok_button().click()
        assert android_login_page.get_reset_password_alert_input_error().text \
            == strings.LOGIN_WRONG_CREDENTIALS_ALERT_MSG
        assert android_login_page.get_reset_password_alert_input_error().text \
            == strings.LOGIN_WRONG_CREDENTIALS_ALERT_MSG
        android_login_page.get_forgot_password_alert_cancel_button().click()

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verify that user cannot login with wrong username and password
        Verify that user cannot login with wrong username and correct password
        Verify that user cannot login with correct username and wrong password
        Verifies that user can login with valid Username and Password
        """

        global_contents = Globals(setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        assert android_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_wrong_password) is False

        assert android_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_password) is False

        assert android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_wrong_password) is False

        android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password)

        if android_whats_new_page.on_screen():
            android_whats_new_page.navigate_features()
            assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
            assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        else:
            android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
            assert android_main_dashboard_page.on_screen() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == global_contents.NEW_LOGISTRATION_ACTIVITY_NAME
        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidLogin.__name__))

    def test_upgrade_app(self, set_capabilities, setup_logging):
        """
        Verifies that user can upgrade app
        """

        global_contents = Globals(setup_logging)
        if not global_contents.jenkins:
            assert global_contents.upgrade_target_app(set_capabilities)
