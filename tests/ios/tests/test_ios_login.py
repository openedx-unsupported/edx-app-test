"""
    Login Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_new_landing import IosNewLanding
from tests.ios.pages.ios_whats_new import IosWhatsNew


class TestIosLogin:
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify Login screen is loaded successfully
        """

        setup_logging.info('-- Starting Test Case')
        global_contents = Globals(setup_logging)
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)

        ios_new_landing_page = IosNewLanding(set_capabilities, setup_logging)
        assert ios_new_landing_page.load_login_screen().text == strings.LOGIN

        setup_logging.info('Login screen successfully loaded')

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
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

        ios_login_page = IosLogin(set_capabilities, setup_logging)

        # Commenting it temporarily, it should be fix with LEARNER-4409
        # textview_screen_title = ios_login_page.get_title_textview()
        # assert textview_screen_title
        # assert textview_screen_title.text == strings.LOGIN_SCREEN_TITLE

        assert ios_login_page.get_logo().text == strings.LOGIN_EDX_LOGO
        assert ios_login_page.get_username_editfield().text == strings.LOGIN_USER_NAME_WATER_MARK
        assert ios_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK
        assert ios_login_page.get_forgot_password_textview().text == strings.LOGIN_FORGOT_PASSWORD
        assert ios_login_page.get_sign_in_button().text == strings.LOGIN
        assert ios_login_page.get_login_with_email_divider_textview().text == strings.LOGIN_IOS_WITH_EMAIL_DIVIDER
        assert ios_login_page.get_facebook_textview().text == strings.LOGIN_FACEBOOK_OPTION
        assert ios_login_page.get_google_textview().text == strings.LOGIN_GOOGLE_OPTION
        assert ios_login_page.get_agreement_textview().text == strings.LOGIN_IOS_AGREEMENT
        assert ios_login_page.get_eula_textview().text == strings.LOGIN_EULA
        assert ios_login_page.get_terms_textview().text == strings.LOGIN_TERMS
        assert ios_login_page.get_privacy_textview().text == strings.LOGIN_PRIVACY

    def test_load_agreement_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping back icon from 'Sign In' screen navigate user back to 'New Landing' screen.
                Verify that user is able to load EULA screen and get back to Login Screen
                Verify that user is able to load Terms screen and get back to Login Screen
                Verify that user is able to load Privacy screen and get back to Login Screen
        """

        ios_login_page = IosLogin(set_capabilities, setup_logging)

        assert ios_login_page.back_and_forth_new_landing()
        # commenting these lines temporary till get the updated id's for these elements
        # assert ios_login_page.load_eula_screen().text == strings.LOGIN
        # assert ios_login_page.load_terms_screen().text == strings.LOGIN
        # assert ios_login_page.load_privacy_screen().text == strings.LOGIN

    def test_forgot_password_alert_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping 'Forgot your password?' will  load 'Reset Password' alert
                Verify following contents are visible on 'Reset Password' alert, 
                Alert Title, Alert Message, Email edit field, Cancel & OK buttons
                Verify tapping 'Ok' will show make email field requied and
                    show email format alert message
                Verify tapping 'Cancel' will close 'Reset Password' alert
        """

        ios_login_page = IosLogin(set_capabilities, setup_logging)

        ios_login_page.get_forgot_password_alert()
        assert ios_login_page.get_forgot_password_alert_title().text == strings.LOGIN_RESET_PASSWORD_ALERT_TITLE
        assert ios_login_page.get_forgot_password_alert_msg().text == strings.LOGIN_RESET_PASSWORD_ALERT_MSG
        assert ios_login_page.get_forgot_password_alert_ok_button().text == strings.LOGIN_RESET_PASSWORD_ALERT_OK
        forgot_password_alert_cancel_button = ios_login_page.get_forgot_password_alert_cancel_button().text
        assert forgot_password_alert_cancel_button == strings.LOGIN_RESET_PASSWORD_ALERT_CANCEL

        ios_login_page.get_forgot_password_alert_ok_button().click()
        assert ios_login_page.get_reset_password_alert_title().text == strings.LOGIN_WRONG_CREDENTIALS_ALERT_TITLE
        assert ios_login_page.get_reset_password_alert_error_message().text \
            == strings.LOGIN_WRONG_CREDENTIALS_ALERT_MSG
        ios_login_page.get_forgot_password_alert_ok_button().click()

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that app shows proper error msg/dialog when user try to login with wrong Username or password
                Verify that user cannot login with wrong username and password
                Verify that user cannot login with wrong username and correct password
                Verify that user cannot login with correct username and wrong password
                Verify that user can login with valid Username and Password
                Verify that user can log out and back to login screen
        """

        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        assert ios_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_password) is False

        assert ios_login_page.login(
            global_contents.login_user_name,
            global_contents.login_wrong_password) is False

        assert ios_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_wrong_password) is False

        ios_login_page.login(global_contents.login_user_name, global_contents.login_password)

        if strings.IS_FIRST_TIME:
            ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
            assert ios_whats_new_page.exit_features().text == strings.BLANK_FIELD

        else:
            setup_logging.info('navigate_features is not needed')

        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        ios_main_dashboard_page.get_drawer_icon().click()
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Landscape support is added for Login screen with following cases,
                Change device orientation to Landscape mode
                Verify following contents are visible on screen, 
                    "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
                    Password edit-field, "Forgot your password?" option, "Sign In" button,
                    "Or sing in with" label, "Facebook" button, "Google" button,
                    "By signing in to this app, you agree to the" label ,
                    "edX Terms of Service and Honor Code" option
                Verify all screen contents have their default values
                Verify tapping back icon from 'Sign In' screen navigate user back to 'New Landing' screen.
                Verify that user is able to load EULA screen and get back to Login Screen
                Verify that user is able to load Terms screen and get back to Login Screen
                Verify that user is able to load Privacy screen and get back to Login Screen
                Verify tapping 'Forgot your password?' will  load 'Reset Password' alert
                Verify following contents are visible on 'Reset Password' alert, 
                Alert Title, Alert Message, Email edit field, Cancel & OK buttons
                Verify tapping 'Cancel' will close 'Reset Password' alert
                Verify that app shows proper error msg/dialog when user try to login with wrong Username or password
                Verifies that user can login with valid Username and Password
        """

        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        assert ios_login_page.get_logo().text == strings.LOGIN_EDX_LOGO
        assert ios_login_page.get_username_editfield().text == strings.LOGIN_USER_NAME_WATER_MARK
        assert ios_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK
        assert ios_login_page.get_forgot_password_textview().text == strings.LOGIN_FORGOT_PASSWORD

        ios_login_page.get_forgot_password_alert()
        assert ios_login_page.get_forgot_password_alert_title().text == strings.LOGIN_RESET_PASSWORD_ALERT_TITLE
        assert ios_login_page.get_forgot_password_alert_msg().text == strings.LOGIN_RESET_PASSWORD_ALERT_MSG
        assert ios_login_page.get_forgot_password_alert_ok_button().text == strings.LOGIN_RESET_PASSWORD_ALERT_OK
        cancel_button_text = ios_login_page.get_forgot_password_alert_cancel_button().text
        assert cancel_button_text == strings.LOGIN_RESET_PASSWORD_ALERT_CANCEL
        assert ios_login_page.close_forgot_password_alert()

        # global_contents.scroll_from_element(set_capabilities, ios_login_page.get_forgot_password_textview())
        assert ios_login_page.get_sign_in_button().text == strings.LOGIN
        assert ios_login_page.get_login_with_email_divider_textview().text == strings.LOGIN_IOS_WITH_EMAIL_DIVIDER
        assert ios_login_page.get_facebook_textview().text == strings.LOGIN_FACEBOOK_OPTION
        assert ios_login_page.get_google_textview().text == strings.LOGIN_GOOGLE_OPTION
        assert ios_login_page.get_agreement_textview().text == strings.LOGIN_IOS_AGREEMENT
        assert ios_login_page.get_eula_textview().text == strings.LOGIN_EULA
        assert ios_login_page.get_terms_textview().text == strings.LOGIN_TERMS
        assert ios_login_page.get_privacy_textview().text == strings.LOGIN_PRIVACY

        assert ios_login_page.back_and_forth_new_landing()
        # commenting these lines temporary till get the updated id's for these elements
        # global_contents.scroll_from_element(set_capabilities, ios_login_page.get_forgot_password_textview())
        # assert ios_login_page.load_eula_screen().text == strings.LOGIN
        # assert ios_login_page.load_terms_screen().text == strings.LOGIN
        # assert ios_login_page.load_privacy_screen().text == strings.LOGIN

        assert ios_login_page.back_and_forth_new_landing()
        assert ios_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_wrong_password
        ) is False

        ios_login_page.login(global_contents.login_user_name, global_contents.login_password)
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_main_dashboard_page.get_drawer_icon().click()
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        landing_page = ios_main_dashboard_page.load_ios_landing_page(set_capabilities, setup_logging)
        assert landing_page.text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('-- Ending Test Case')

    def test_upgrade_app(self, set_capabilities, setup_logging):
        """
        Verifies that user can upgrade app
        """

        global_contents = Globals(setup_logging)
        assert global_contents.upgrade_target_app(set_capabilities)
