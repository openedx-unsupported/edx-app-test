"""
    Register Test Module
"""

from common import strings
from ios.pages.ios_new_landing import IosNewLanding
from ios.pages.ios_register import IosRegister


class TestIosRegister(object):
    """
        Register Screen Test Case
    """

    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestIosRegister.__name__))

        ios_new_landing_page = IosNewLanding(set_capabilities, setup_logging)
        ios_register_page = IosRegister(set_capabilities, setup_logging)

        ios_new_landing_page.load_register_screen()
        assert ios_register_page.get_register_divider_textview().text == strings.REGISTER_SCREEN_REGISTER_WITH

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
        assert ios_register_page.get_register_divider_textview().text == strings.REGISTER_SCREEN_REGISTER_WITH
        assert ios_register_page.get_facebook_textview().text == strings.LOGIN_FACEBOOK_OPTION
        assert ios_register_page.get_google_textview().text == strings.LOGIN_GOOGLE_OPTION

        email_divider = ios_register_page.get_register_with_email_divider_textview()
        assert email_divider.text == strings.REGISTER_WITH_EMAIL_DIVIDER
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

        setup_logging.info('-- Ending {} Test Case'.format(TestIosRegister.__name__))
