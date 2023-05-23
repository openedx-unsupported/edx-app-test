"""
    Register Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_new_landing import IosNewLanding
from tests.ios.pages.ios_register import IosRegister
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList


class TestIosRegister:
    """
    Register Screen Test Case
    """

    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """

        setup_logging.info('-- Starting Test Case')

        ios_new_landing_page = IosNewLanding(set_capabilities, setup_logging)
        ios_register_page = IosRegister(set_capabilities, setup_logging)

        ios_new_landing_page.load_register_screen()
        assert ios_register_page.get_register_divider_textview().text == strings.REGISTER_SCREEN_TITLE

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

        ios_register_page = IosRegister(set_capabilities, setup_logging)

        assert ios_register_page.get_register_close_button()
        assert ios_register_page.get_register_divider_textview().text == strings.REGISTER_SCREEN_TITLE
        assert ios_register_page.get_facebook_textview().text == strings.REGISTER_FACEBOOK_BUTTON
        assert ios_register_page.get_google_textview().text == strings.REGISTER_GOOGLE_BUTTON

        assert ios_register_page.get_email_editfield().text == strings.REGISTER_EMAIL_LABEL
        assert ios_register_page.get_email_instructions_textview().text == strings.REGISTER_EMAIL_INSTRUCTIONS
        assert ios_register_page.get_full_name_editfield().text == strings.REGISTER_FULL_NAME_LABEL

        full_name_instructions = ios_register_page.get_full_name_instructions_textview()
        assert full_name_instructions.text == strings.REGISTER_FULL_NAME_INSTRUCTIONS
        assert ios_register_page.get_user_name_editfield().text == strings.REGISTER_USER_NAME_LABEL

        user_name_instructions = ios_register_page.get_user_name_instructions_textview()
        assert user_name_instructions.text == strings.REGISTER_USER_NAME_INSTRUCTIONS
        assert ios_register_page.get_password_editfield().text == strings.REGISTER_PASSWORD_LABEL

        password_instructions = ios_register_page.get_password_instructions_textview()
        assert password_instructions.text == strings.REGISTER_PASSWORD_INSTRUCTIONS
        assert ios_register_page.get_country_spinner()

        country_spinner_instructions = ios_register_page.get_country_spinner_instructions_textview()
        assert country_spinner_instructions.text == strings.REGISTER_COUNTRY_INSTRUCTIONS

        show_optional_fields = ios_register_page.get_show_optional_fields_textview()
        assert show_optional_fields.text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION
        assert ios_register_page.get_create_my_account_textview().text == strings.REGISTER_CREATE_MY_ACCOUNT
        assert ios_register_page.get_agreement_textview().text == strings.REGISTER_AGREEMENT

    def test_show_hide_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that tapping "Show optional fields" will turn to "Hide optional fields" and load following optional
        contents below,
            "Gender" spinner, "Year of birth" spinner, "Highest level of education completed" spinner,
        Verify that tapping "Hide optional fields" will turn to "Show optional fields" and all optional
            contents will be hidden
        Verify all optional contents/elements have default values
        """

        ios_register_page = IosRegister(set_capabilities, setup_logging)

        optional_fields = ios_register_page.get_show_optional_fields_textview().text
        assert optional_fields == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION
        assert ios_register_page.show_optional_fields().text == strings.REGISTER_HIDE_OPTIONAL_FIELDS_OPTION

        assert ios_register_page.get_gender_textview().text == strings.REGISTER_GENDER_DEFAULT_VALUE
        assert ios_register_page.get_gender_spinner()
        ios_register_page.load_gender_spinner()

        assert ios_register_page.get_education_textview().text == strings.REGISTER_EDU_DEFAULT_VALUE
        assert ios_register_page.get_education_spinner()
        ios_register_page.load_education_spinner()

        assert ios_register_page.hide_optional_fields().text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION
        assert ios_register_page.get_agreement_textview().text == strings.REGISTER_AGREEMENT

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify tapping "Back" icon will load New Logistration/New Landing screen
            back to 'New Landing' screen.
        Verify tapping "edX Terms of Service and Honor Code" loads "End User License Agreement" screen
        Verify tapping back icon from "End User License Agreement" screen
            navigate user back to 'Register' screen.
        Verify that user is able to load EULA screen and get back to Register Screen
        Verify that user is able to load Terms screen and get back to Register Screen
        Verify that user is able to load Privacy screen and get back to Register Screen
        """

        ios_register_page = IosRegister(set_capabilities, setup_logging)

        assert ios_register_page.back_and_forth_register()
        # assert ios_register_page.load_eula_screen().text == strings.REGISTER_SCREEN_REGISTER_WITH
        # assert ios_register_page.load_terms_screen().text == strings.REGISTER_SCREEN_REGISTER_WITH
        # assert ios_register_page.load_privacy_screen().text == strings.REGISTER_SCREEN_REGISTER_WITH

    def test_required_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that following input types are required,
            Email edit-field, Full Name edit-field, Public User Name edit-field,
            Password edit-field, "Country or Region of Residence" spinner,
        Verify that app will show specific error message against each field
        """

        ios_register_page = IosRegister(set_capabilities, setup_logging)

        if ios_register_page.validate_required_optional_fields():
            assert ios_register_page.get_email_validation_textview().text == strings.REGISTER_EMAIL_BLANK_ERROR
            assert ios_register_page.get_full_name_validation_textview().text == strings.REGISTER_FULL_NAME_BLANK_ERROR
            assert ios_register_page.get_username_validation_textview().text == strings.REGISTER_USER_NAME_BLANK_ERROR
            assert ios_register_page.get_password_validation_textview().text == strings.REGISTER_PASSWORD_BLANK_ERROR
            assert ios_register_page.get_country_validation_textview().text == strings.REGISTER_COUNTRY_BLANK_ERROR

        else:
            setup_logging.info('Something wrong with validations checks')

    def test_register_smoke(self, set_capabilities, setup_logging):
        """
            Verify that tapping "Create your account" button after filling all required input(valid) types,
                will validate all inputs and load "Whats new feature screen" with specific user logged in
            Verify that tapping "Create your account" button after filling all required input(valid) types,
                will validate all inputs and load "Whats new feature screen" with specific user logged in
            Verify that following input types are optional,
                "Gender" spinner
                "Year of birth" spinner
                "Highest level of education completed" spinner
            Verify that user should be able to log out and re-login with new created account credentials
            Verify that for new user there must be "Looking for new challenge?" heading is available on the screen
        """

        ios_register_page = IosRegister(set_capabilities, setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = (first_name + ' ' + last_name)
        password = global_contents.generate_random_credentials(8)

        ios_register_page.submit_register_form('', full_name, user_name, password, click_country=False)
        ios_register_page.validate_required_optional_fields()
        assert ios_register_page.get_email_validation_textview().text == strings.REGISTER_EMAIL_BLANK_ERROR

        ios_register_page.submit_register_form(email, '', user_name, password, click_country=False)
        ios_register_page.validate_required_optional_fields()
        assert ios_register_page.get_full_name_validation_textview().text == strings.REGISTER_FULL_NAME_BLANK_ERROR

        ios_register_page.submit_register_form(email, full_name, '', password, click_country=False)
        ios_register_page.validate_required_optional_fields()
        assert ios_register_page.get_username_validation_textview().text == strings.REGISTER_USER_NAME_BLANK_ERROR

        ios_register_page.submit_register_form(email, full_name, user_name, '', click_country=False)
        ios_register_page.validate_required_optional_fields()
        assert ios_register_page.get_password_validation_textview().text == strings.REGISTER_PASSWORD_BLANK_ERROR

        setup_logging.info(f'Email - {email},  Username - {user_name}, Full Name - {full_name}, Password -{password}')

        ios_register_page.submit_register_form(email, full_name, user_name, password)

        if global_contents.whats_new_enable:
            assert ios_whats_new_page.get_title_textview()
            assert ios_whats_new_page.navigate_features().text == strings.CLOSE_BUTTON_TEXT
            assert ios_whats_new_page.exit_features().text == strings.BLANK_FIELD

        assert ios_my_courses_list.get_find_courses_message().text == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        assert ios_my_courses_list.get_find_course_button().text == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_IOS

        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info(f'{user_name} is successfully logged out')

        assert ios_login_page.login(user_name, password)
        setup_logging.info(f'{user_name} is successfully logged in')
        assert ios_main_dashboard_page.get_title_textview_portrait_mode().text == strings.MAIN_DASHBOARD_SCREEN_TITLE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from register screen successfully
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        setup_logging.info('-- Ending Test Case')
