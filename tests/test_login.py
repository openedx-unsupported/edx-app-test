from pages.login import Login
from pages.new_logistration import NewLogistration
from common.strings import Strings
from common.globals import Globals
from testdata.input_data import InputData


class TestLogin():
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities):
        """
        Scenarios:
            Verify Login screen is loaded successfully
        """

        print('-- Starting ', TestLogin.__name__, 'Test Case')
        new_logistration_page = NewLogistration(set_capabilities)

        if InputData.target_environment == Strings.ANDROID:
            assert new_logistration_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
            print('Login screen successfully loaded')

        elif InputData.target_environment == Strings.IOS:
            assert new_logistration_page.load_login_screen().text == Strings.LOGIN_SCREEN_TITLE
            print('Login screen successfully loaded')

    def test_ui_elements(self, set_capabilities):
        """
        Verify following contents are visible on screen, 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button, "Or sing in with" label 
            "Facebook" button, "Google" button, "By signing in to this app, you agree to the" label 
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values

        """

        login_page = Login(set_capabilities)
        textview_screen_title = login_page.get_title_textview()
        assert textview_screen_title is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_screen_title.text == Strings.LOGIN_SCREEN_TITLE

        #assert login_page.get_logo() is not None

        editfield_user_name = login_page.get_username_editfield()
        assert editfield_user_name is not None
        if InputData.target_environment == Strings.IOS:
            assert editfield_user_name.text == Strings.LOGIN_USER_NAME_WATER_MARK

        editfield_password = login_page.get_password_editfield()
        assert editfield_password is not None
        if InputData.target_environment == Strings.IOS:
            assert editfield_password.text == Strings.LOGIN_PASSWORD_WATER_MARK

        textview_forget_password = login_page.get_forget_password_textview()
        assert textview_forget_password is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_forget_password.text == Strings.LOGIN_FORGET_PASSWORD

        button_sing_in = login_page.get_sign_in_button()
        assert button_sing_in is not None
        if InputData.target_environment == Strings.IOS:
            assert button_sing_in.text == Strings.LOGIN

        textview_login_with_email_divider = login_page.get_login_with_email_divider_textview()
        assert textview_login_with_email_divider is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_login_with_email_divider.text == Strings.LOGIN_IOS_WITH_EMAIL_DIVIDER

        textview_facebook = login_page.get_facebook_textview()
        assert textview_facebook is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_facebook.text == Strings.LOGIN_FACBOOK_OPTION

        textview_google = login_page.get_google_textview()
        assert textview_google is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_google.text == Strings.LOGIN_GOOGLE_OPTION

        textview_agree = login_page.get_agree_textview()
        assert textview_agree is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_agree.text == Strings.LOGIN_AGREE

        textview_terms = login_page.get_terms_textview()
        assert textview_terms is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_terms.text == Strings.LOGIN_IOS_TERMS

    def test_login_smoke(self, set_capabilities):
        """
        Verifies that user can login with valid Username and Password
        """

        login_page = Login(set_capabilities)

        if InputData.target_environment == Strings.ANDROID:
            assert login_page.login(InputData.login_user_name, InputData.login_password) == \
                   Globals.WHATS_NEW_ACTIVITY_NAME

        elif InputData.target_environment == Strings.IOS:
            assert login_page.login(InputData.login_user_name, InputData.login_password).text ==\
                   Strings.WHATS_NEW_IOS_SCREEN_TITLE

        print(InputData.target_environment, 'is successfully logged in')
        print('-- Ending ', TestLogin.__name__, 'Test Case')