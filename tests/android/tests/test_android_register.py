# coding=utf-8
"""
    Register Test Module
"""
from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_register import AndroidRegister
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common.globals import Globals
from tests.common import strings


class TestAndroidRegister:
    """
        Register Screen Test Case
    """

    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidRegister.__name__))

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

        assert android_register_page.get_register_divider_textview().text == strings.REGISTER_SCREEN_REGISTER_WITH
        assert android_register_page.get_facebook_textview().text == strings.FACEBOOK_OPTION
        assert android_register_page.get_google_textview().text == strings.GOOGLE_OPTION

        email_divider = android_register_page.get_register_with_email_divider_textview()
        assert email_divider.text == strings.REGISTER_SCREEN_REGISTER_WITH
        android_register_page.page_scroll_down()
        assert android_register_page.get_email_editfield().text == strings.REGISTER_EMAIL_LABEL
        assert android_register_page.get_email_instructions_textview().text == strings.REGISTER_EMAIL_INSTRUCTIONS
        assert android_register_page.get_full_name_editfield().text == strings.REGISTER_FULL_NAME_LABEL

        full_name_instructions = android_register_page.get_full_name_instructions_textview()
        assert full_name_instructions.text == strings.REGISTER_FULL_NAME_INSTRUCTIONS
        assert android_register_page.get_user_name_editfield().text == strings.REGISTER_USER_NAME_LABEL

        user_name_instructions = android_register_page.get_user_name_instructions_textview()
        assert user_name_instructions.text == strings.REGISTER_USER_NAME_INSTRUCTIONS
        assert android_register_page.get_password_editfield().text == strings.REGISTER_PASSWORD_LABEL

        password_instructions = android_register_page.get_password_instructions_textview()
        assert password_instructions.text == strings.REGISTER_PASSWORD_INSTRUCTIONS
        assert android_register_page.get_country_spinner().text == strings.REGISTER_COUNTRY_DEFAULT_VALUE

        android_register_page.page_scroll_down()
        assert android_register_page.get_create_my_account_textview().text == strings.REGISTER_CREATE_MY_ACCOUNT
        show_optional_fields = android_register_page.get_show_optional_fields_textview()
        assert show_optional_fields.text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION
        country_spinner_instructions = android_register_page.get_country_spinner_instructions_textview()
        assert country_spinner_instructions.text == strings.REGISTER_COUNTRY_INSTRUCTIONS
        assert android_register_page.get_agreement_textview().text == strings.REGISTER_AGREEMENT_ANDROID

    def test_show_hide_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that tapping "Show optional fields" will turn to "Hide optional fields" and load following optional
        contents below,
            "Gender" spinner, "Year of birth" spinner, "Highest level of education completed" spinner,
            "Tell us why you're interested in edX" label with edit-field below,
        Verify that tapping "Hide optional fields" will turn to "Show optional fields" and all optional
            contents will be hidden
        Verify all optional contents/elements have default values
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        assert android_register_page.show_hide_optional_fields().text == strings.REGISTER_HIDE_OPTIONAL_FIELDS_OPTION

        assert android_register_page.get_gender_spinner().text == strings.REGISTER_GENDER_DEFAULT_VALUE
        assert android_register_page.get_year_of_birth_spinner().text == strings.REGISTER_YOB_DEFAULT_VALUE
        assert android_register_page.get_eduction_spinner().text == strings.REGISTER_EDU_DEFAULT_VALUE
        assert android_register_page.get_why_interested_editfield().text == strings.REGISTER_INTERESTED_DEFAULT_VALUE
        assert android_register_page.show_hide_optional_fields().text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping "Back" icon will load New Logistration/New Landing screen
                    back to 'New Logistration' screen.
                Verify tapping "edX Terms of Service and Honor Code" loads "End User License Agreement" screen
                Verify tapping back icon from "End User License Agreement" screen
                    navigate user back to 'Register' screen.
                Verify that user is able to load EULA screen and get back to Register Screen
                Verify that user is able to load Terms screen and get back to Register Screen
                Verify that user is able to load Privacy screen and get back to Register Screen
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        assert android_register_page.back_and_forth_register()
        # assert android_register_page.load_eula_screen()
        # assert android_register_page.load_terms_screen()
        # assert android_register_page.load_privacy_screen()

    def test_required_and_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that following input types are required,
            Email editfield, Full Name editfield, Public, User Name, editfield, Password editfield,
            "Country or Region of Residence" spinner
        Verify that following input types are optional,
            "Gender" spinner, "Year of birth" spinner, "Highest level of education completed" spinner,
            "Tell us why you're interested in edX" label with edit - field below
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)
        assert android_register_page.validate_required_optional_fields()
        assert android_register_page.get_email_validation_textview().text == strings.REGISTER_EMAIL_BLANK_ERROR
        assert android_register_page.get_full_name_validation_textview().text == strings.REGISTER_FULL_NAME_BLANK_ERROR
        assert android_register_page.get_username_validation_textview().text == strings.REGISTER_USER_NAME_BLANK_ERROR
        assert android_register_page.get_password_validation_textview().text == strings.REGISTER_PASSWORD_BLANK_ERROR
        assert android_register_page.get_country_validation_textview().text == strings.REGISTER_COUNTRY_BLANK_ERROR

    def test_register_smoke(self, set_capabilities, setup_logging):
        """
        Verify that tapping "Create your account" button after filling all required input(valid) types,
            will validate all inputs and load "Whats new feature screen" with specific user logged in
        Verify that user should be able to log out and re-login with new created account credentials
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
        setup_logging.info('Email - {},  Username - {}, Full Name - {}, Password -{}'.format(
            email,
            user_name,
            full_name,
            password
        ))

        android_register_page.back_and_forth_register()
        android_register_page.register(email,
                                       full_name,
                                       user_name,
                                       password,
                                       global_contents.country
                                       )

        global_contents.wait_for_android_activity_to_load(
            set_capabilities,
            global_contents.REGISTER_ACTIVITY_NAME
        )

        if android_whats_new_page.on_screen():
            android_whats_new_page.navigate_features()
            assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
            assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))
        else:
            assert android_main_dashboard_page.on_screen() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        login_output = android_login_page.login(
            user_name,
            password,
            False)

        assert login_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(user_name))

        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidRegister.__name__))
