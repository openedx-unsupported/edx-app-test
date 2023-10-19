"""
    Register Test Module
"""

from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_register import AndroidRegister
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidRegister:
    """
        Register Screen Test Case
    """

    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """

        setup_logging.info('Starting {} Test Case'.format(TestAndroidRegister.__name__))

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        android_new_landing_page.load_register_screen()
        assert android_register_page.on_screen() == Globals.REGISTER_ACTIVITY_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify following contents are visible on screen,
            "Register with" label, "Facebook" button
            "Google" button, "or register with email" label, Email edit-field,
            "This is what you will use to login" label below, Full Name edit-field,
            "The name will be used on any certificates that you earn" label below,
            Public User Name edit-field,
            "The name that will identify you in your courses. It cannot be changed later." label below,
            Password edit-field, "Your password must contain at least 8 characters, including 1 letter & 1 number.",
            "Country or Region of Residence" spinner,
            "The country or region where you live." label below, "Show optional fields" option below,
            "Create my account" button,
            "By creating an account you agree to the "edX Terms of Service and Honor Code" option
        Verify all contents/elements have default value
        Verify that user should be able to scroll screen to see all contents
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)
        assert android_register_page.get_full_name_editfield().text == strings.REGISTER_FULL_NAME_LABEL
        assert android_register_page.get_user_name_editfield().text == strings.REGISTER_USER_NAME_LABEL
        assert android_register_page.get_email_editfield().text == strings.REGISTER_EMAIL_LABEL
        assert android_register_page.get_password_editfield().text == strings.REGISTER_PASSWORD_LABEL
        assert android_register_page.get_show_password_button().get_attribute(
            'content-desc') == strings.REGISTER_SHOW_PASSWORD
        assert android_register_page.get_country_spinner().text == strings.REGISTER_COUNTRY_DEFAULT_VALUE
        assert android_register_page.get_show_optional_fields().text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION
        android_register_page.get_show_optional_fields().click()
        assert android_register_page.get_eduction_spinner().text == strings.REGISTER_EDU_DEFAULT_VALUE
        assert android_register_page.get_gender_spinner().text == strings.REGISTER_GENDER_DEFAULT_VALUE
        android_register_page.get_show_optional_fields().click()
        assert android_register_page.get_register_checkbox().text == strings.REGISTER_CHECKBOX
        assert android_register_page.get_eula_element().text == strings.REGISTER_AGREEMENT_ANDROID
        android_register_page.page_scroll_down()
        assert android_register_page.get_create_my_account_textview().get_attribute(
            'content-desc') == strings.REGISTER_CREATE_MY_ACCOUNT
        assert android_register_page.get_google_textview().text == strings.GOOGLE_OPTION
        assert android_register_page.get_facebook_textview().text == strings.FACEBOOK_OPTION
        assert android_register_page.get_microsoft_login_textview().text == strings.MICROSOFT_LOGIN_BUTTON

    def test_required_and_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that following input types are required,
            Email editfield, Full Name editfield, Public, User Name, editfield, Password editfield,
            "Country or Region of Residence" spinner
        Verify that following input types are optional,
            "Gender" spinner, "Year of birth" spinner, "Highest level of education completed" spinner,
            "Tell us why you're interested in edX" label with edit - field below
        Verify that, if user fill all data except "Full Name" and tap on 'Create my account' button,
            alert pop up should appear along with the error message.
        Verify that, if user fill all data except "User Name" and tap on 'Create my account' button,
            alert pop up should appear along with the error message.
        Verify that, if user fill all data except "Password" and tap on 'Create my account' button,
            alert pop up should appear along with the error message.
        Verify that, if user fill all data except "Country" and tap on 'Create my account' button,
            alert pop up should appear along with the error message.
        Verify that, if user fill all data but with wrong email format and tap on 'Create my account' button,
            email format error message should appear.
        Verify that, if user fill all data but with wrong email format and tap on 'Create my account' button,
            email format error message should appear.
        Verify that, password required at least 8 characters with special character in it.
        """

        global_contents = Globals(setup_logging)
        android_register_page = AndroidRegister(set_capabilities, setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)

        set_capabilities.back()
        android_new_landing_page.load_register_screen()
        assert android_register_page.on_screen() == Globals.REGISTER_ACTIVITY_NAME
        assert android_register_page.validate_required_optional_fields()
        assert android_register_page.get_full_name_validation_textview().text == strings.REGISTER_FULL_NAME_BLANK_ERROR
        assert android_register_page.get_username_validation_textview().text == strings.REGISTER_USER_NAME_BLANK_ERROR
        assert android_register_page.get_email_validation_textview().text == strings.REGISTER_EMAIL_BLANK_ERROR
        assert android_register_page.get_password_validation_textview().text == strings.REGISTER_PASSWORD_BLANK_ERROR
        assert android_register_page.get_country_validation_textview().text == strings.REGISTER_COUNTRY_BLANK_ERROR

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        name = "{} {}".format(first_name, last_name)
        full_name = name
        password = global_contents.generate_random_credentials(8)
        android_register_page.register(email,
                                       '',
                                       user_name,
                                       password,
                                       global_contents.country
                                       )

        assert android_register_page.validate_required_optional_fields()
        assert android_register_page.get_full_name_validation_textview().text == strings.REGISTER_FULL_NAME_BLANK_ERROR

        android_register_page.register(email,
                                       full_name,
                                       '',
                                       password,
                                       global_contents.country
                                       )
        assert android_register_page.validate_required_optional_fields()

        android_register_page.register(email,
                                       full_name,
                                       user_name,
                                       '',
                                       global_contents.country
                                       )
        assert android_register_page.validate_required_optional_fields()

        android_register_page.register(email,
                                       full_name,
                                       user_name,
                                       password,
                                       ''
                                       )
        assert android_register_page.validate_required_optional_fields()

        android_register_page.register(email,
                                       full_name,
                                       user_name,
                                       'xxxxxxxx',
                                       global_contents.country
                                       )
        assert android_register_page.validate_required_optional_fields()

        android_register_page.register('xxxx@xxxxx',
                                       full_name,
                                       user_name,
                                       password,
                                       global_contents.country
                                       )
        assert android_register_page.validate_required_optional_fields()
        assert android_register_page.get_email_format_validation_textview().text \
            == strings.LOGIN_WRONG_CREDENTIALS_ALERT_MSG

    def test_register_smoke(self, set_capabilities, setup_logging):
        """
        Verify that tapping "Create your account" button after filling all required input(valid) types,
            will validate all inputs and load "Whats new feature screen" with specific user logged in
        Verify that user should be able to re-login with new created account credentials
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        name = first_name + ' ' + last_name
        full_name = name
        password = global_contents.generate_random_credentials(8)
        setup_logging.info(f'Email - {email},  Username - {user_name}, Full Name - {full_name}, Password -{password}')

        android_register_page.back_and_forth_register()
        android_register_page.register(email,
                                       full_name,
                                       user_name,
                                       password,
                                       global_contents.country
                                       )

        assert android_register_page.get_create_my_account_textview().get_attribute(
            'content-desc') == 'Create an account'
        android_register_page.get_create_my_account_textview().click()

        if global_contents.whats_new_enable:
            android_whats_new_page.navigate_features()
            assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
            assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
            setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')
        else:
            assert android_main_dashboard_page.on_screen() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        profile_tab.click()

        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        login_output = android_login_page.login(
            user_name,
            password,
            False)

        assert login_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info(f'{user_name} is successfully logged in')

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from my register screen
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        profile_tab.click()
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')

        setup_logging.info(f'Ending {TestAndroidRegister.__name__} Test Case')
