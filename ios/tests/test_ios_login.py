
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
        assert ios_new_logistration_page.load_login_screen().text == strings.LOGIN

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

        ios_login_page = IosLogin(set_capabilities, setup_logging)

        # Commenting it temporarily, it should be fix with LEARNER-3888
        # textview_screen_title = ios_login_page.get_title_textview()
        # assert textview_screen_title
        # assert textview_screen_title.text == strings.LOGIN_SCREEN_TITLE

        assert ios_login_page.get_logo().text == strings.LOGIN_EDX_LOGO

        assert ios_login_page.get_username_editfield().text == strings.LOGIN_USER_NAME_WATER_MARK

        assert ios_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK

        assert ios_login_page.get_forget_password_textview().text == strings.LOGIN_FORGOT_PASSWORD

        assert ios_login_page.get_sign_in_button().text == strings.LOGIN

        assert ios_login_page.get_login_with_email_divider_textview().text == strings.LOGIN_IOS_WITH_EMAIL_DIVIDER

        assert ios_login_page.get_facebook_textview().text == strings.LOGIN_FACEBOOK_OPTION

        assert ios_login_page.get_google_textview().text == strings.LOGIN_GOOGLE_OPTION

        assert ios_login_page.get_agree_textview().text == strings.LOGIN_AGREE

        assert ios_login_page.get_terms_textview().text == strings.LOGIN_IOS_TERMS

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
