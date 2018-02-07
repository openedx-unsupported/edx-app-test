"""
    Login Test Module
"""
from common.globals import Globals
from input_data import InputData
from android.pages.android_new_logistration import AndroidNewLogistration
from android.pages.android_login import AndroidLogin
from common import strings

class TestAndroidLogin:
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Login screen is loaded successfully
        """

        log = setup_logging
        log.info('-- Starting {} Test Case'.format(TestAndroidLogin.__name__))

        android_new_logistration_page = AndroidNewLogistration(set_capabilities, setup_logging)
        assert android_new_logistration_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        log.info('Login screen successfully loaded')

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen, 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label ,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        textview_screen_title = android_login_page.get_title_textview()
        assert textview_screen_title.text == strings.LOGIN

        editfield_user_name = android_login_page.get_username_editfield()
        assert editfield_user_name.text == strings.BLANK_FIELD

        editfield_password = android_login_page.get_password_editfield()
        assert editfield_password.text == strings.BLANK_FIELD

        textview_forgot_password = android_login_page.get_forgot_password_textview()
        assert textview_forgot_password.text == strings.LOGIN_FORGOT_PASSWORD

        button_sing_in = android_login_page.get_sign_in_button()
        assert button_sing_in.text == strings.LOGIN

        textview_login_with_email_divider = android_login_page.get_login_with_email_divider_textview()
        assert textview_login_with_email_divider.text == strings.LOGIN_ANDROID_WITH_EMAIL_DIVIDER

        textview_facebook = android_login_page.get_facebook_textview()
        assert textview_facebook.text == strings.FACEBOOK_OPTION

        textview_google = android_login_page.get_google_textview()
        assert textview_google.text == strings.GOOGLE_OPTION

        textview_agree = android_login_page.get_agree_textview()
        assert textview_agree.text == strings.LOGIN_AGREE

        textview_terms = android_login_page.get_terms_textview()
        assert textview_terms.text == strings.LOGIN_ANDROID_TERMS

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping back icon from 'Sign In' screen navigate user
                    back to 'New Logistration' screen.
                Verify tapping "edX Terms of Service and Honor Code" loads "End User License Agreement" screen
                Verify tapping back icon from "End User License Agreement" screen
                    navigate user back to 'Sign In' screen.
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        assert android_login_page.back_and_forth_login()
        assert android_login_page.back_and_forth_terms()

    def test_forgot_password_alert(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping 'Forgot your password?' will  load 'Reset Password' alert
                Verify following contents are visible on 'Reset Password' alert, 
                Alert Title, Alert Message, Email edit field, Cancel & OK buttons
                Verify tapping 'Cancel' will close 'Reset Password' alert
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_login_page.get_forgot_password_alert()

        textview_alert_title = android_login_page.get_forgot_password_alert_title()
        assert textview_alert_title.text == strings.LOGIN_RESET_PASSWORD_ALERT_TITLE

        textview_alert_msg = android_login_page.get_forgot_password_alert_msg()
        assert textview_alert_msg.text == strings.LOGIN_RESET_PASSWORD_ALERT_MSG

        button_alert_ok = android_login_page.get_forgot_password_alert_ok_button()
        assert button_alert_ok.text == strings.LOGIN_RESET_PASSWORD_ALERT_OK

        button_alert_cancel = android_login_page.get_forgot_password_alert_cancel_button()

        assert button_alert_cancel.text == strings.LOGIN_RESET_PASSWORD_ALERT_CANCEL

        assert android_login_page.close_forgot_password_alert()

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can login with valid Username and Password
        """

        log = setup_logging
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        login_output = android_login_page.login(InputData.login_user_name, InputData.login_password)
        assert login_output == Globals.WHATS_NEW_ACTIVITY_NAME
        log.info('{} is successfully logged in'.format(InputData.login_user_name))
        log.info('-- Ending {} Test Case'.format(TestAndroidLogin.__name__))
