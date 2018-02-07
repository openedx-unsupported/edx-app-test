"""
    Login Test Module
"""

from common import strings
from common.globals import Globals
from input_data import InputData
from ios.pages.ios_new_logistration import IosNewLogistration
from ios.pages.ios_login import IosLogin

class TestIosLogin:
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Login screen is loaded successfully
        """
        log = setup_logging
        log.info('-- Starting {} Test Case'.format(TestIosLogin.__name__))

        ios_new_logistration_page = IosNewLogistration(set_capabilities, setup_logging)
        assert ios_new_logistration_page.load_login_screen().text == strings.LOGIN_SCREEN_TITLE
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
        ios_login_page = IosLogin(set_capabilities, setup_logging)

        textview_screen_title = ios_login_page.get_title_textview()
        assert textview_screen_title is not None
        assert textview_screen_title.text == strings.LOGIN_SCREEN_TITLE

        editfield_user_name = ios_login_page.get_username_editfield()
        assert editfield_user_name is not None
        assert editfield_user_name.text == strings.LOGIN_USER_NAME_WATER_MARK

        editfield_password = ios_login_page.get_password_editfield()
        assert editfield_password is not None
        assert editfield_password.text == strings.LOGIN_PASSWORD_WATER_MARK

        textview_forget_password = ios_login_page.get_forget_password_textview()
        assert textview_forget_password is not None
        assert textview_forget_password.text == strings.LOGIN_FORGOT_PASSWORD

        button_sing_in = ios_login_page.get_sign_in_button()
        assert button_sing_in is not None
        assert button_sing_in.text == strings.LOGIN

        textview_login_with_email_divider = ios_login_page.get_login_with_email_divider_textview()
        assert textview_login_with_email_divider is not None
        assert textview_login_with_email_divider.text == strings.LOGIN_IOS_WITH_EMAIL_DIVIDER

        textview_facebook = ios_login_page.get_facebook_textview()
        assert textview_facebook is not None
        assert textview_facebook.text == strings.LOGIN_FACBOOK_OPTION

        textview_google = ios_login_page.get_google_textview()
        assert textview_google is not None
        assert textview_google.text == strings.LOGIN_GOOGLE_OPTION

        textview_agree = ios_login_page.get_agree_textview()
        assert textview_agree is not None
        assert textview_agree.text == strings.LOGIN_AGREE

        textview_terms = ios_login_page.get_terms_textview()
        assert textview_terms is not None
        assert textview_terms.text == strings.LOGIN_IOS_TERMS

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can login with valid Username and Password
        """
        log = setup_logging
        global_contents = Globals(log)

        ios_login_page = IosLogin(set_capabilities, setup_logging)

        login_output = ios_login_page.login(InputData.login_user_name, InputData.login_password).text

        if global_contents.is_first_time:
            assert login_output == strings.WHATS_NEW_IOS_SCREEN_TITLE
        else:
            assert login_output == strings.MAIN_DASHBOARD_SCREEN_TITLE

        log.info('{} is successfully logged in'.format(InputData.target_environment))
        log.info('-- Ending {} Test Case'.format(TestIosLogin.__name__))
