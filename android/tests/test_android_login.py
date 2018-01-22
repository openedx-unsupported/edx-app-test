"""
    Login Test Module
"""

from common.globals import Globals
from conftest import setup_logging
from input_data import InputData
from android.pages.android_new_logistration import AndroidNewLogistration
from android.pages.android_login import AndroidLogin



class TestAndroidLogin:
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Login screen is loaded successfully
        """
        log = setup_logging
        log.info('-- Starting {} Test Case'.format(TestAndroidLogin.__name__))

        android_new_logistration_page = AndroidNewLogistration(set_capabilities, setup_logging)
        assert android_new_logistration_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        log.info('Login screen successfully loaded')

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Verify following contents are visible on screen, 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label ,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values

        """
        log = setup_logging

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        textview_screen_title = android_login_page.get_title_textview()
        assert textview_screen_title is not None

        editfield_user_name = android_login_page.get_username_editfield()
        assert editfield_user_name is not None

        editfield_password = android_login_page.get_password_editfield()
        assert editfield_password is not None

        textview_forget_password = android_login_page.get_forget_password_textview()
        assert textview_forget_password is not None

        button_sing_in = android_login_page.get_sign_in_button()
        assert button_sing_in is not None

        textview_login_with_email_divider = android_login_page.get_login_with_email_divider_textview()
        assert textview_login_with_email_divider is not None

        textview_facebook = android_login_page.get_facebook_textview()
        assert textview_facebook is not None

        textview_google = android_login_page.get_google_textview()
        assert textview_google is not None

        textview_agree = android_login_page.get_agree_textview()
        assert textview_agree is not None

        textview_terms = android_login_page.get_terms_textview()
        assert textview_terms is not None

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can login with valid Username and Password
        """
        log = setup_logging
        global_contents = Globals(log)

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        login_output = android_login_page.login(InputData.login_user_name, InputData.login_password)
        assert login_output == Globals.WHATS_NEW_ACTIVITY_NAME

        log.info(InputData.target_environment + ' is successfully logged in')
        log.info('-- Ending {} Test Case'.format(TestAndroidLogin.__name__ ))
