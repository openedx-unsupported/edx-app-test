# coding=utf-8
"""
    Register Page Module
"""
from common import strings
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage
from ios.pages.ios_new_landing import IosNewLanding


class IosRegister(IosBasePage):
    """
    Register screen
    """

    def get_register_close_button(self):
        """
        Get Register With Divider

        Returns:
              webdriver element: Register With Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_close_button
        )

    def get_register_divider_textview(self):
        """
        Get Register With Divider

        Returns:
              webdriver element: Register With Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_divider_textview
        )

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
              webdriver element: Facebook Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_facebook_textview
        )

    def get_google_textview(self):
        """
        Get Google

        Returns:
              webdriver element: Google Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_google_textview
        )

    def get_register_with_email_divider_textview(self):
        """
        Get Register With Email Divider

        Returns:
              webdriver element: Register With Email Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_with_email_divider_textview
        )

    def get_email_editfield_label(self):
        """
        Get Email label

        Returns:
              webdriver element: Email label Element
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_email_label
        )

    def get_email_editfield(self):
        """
        Get Email

        Returns:
              webdriver element: Email Element
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_email_textfield
        )

    def get_email_instructions_textview(self):
        """
        Get Email Instructions

        Returns:
              webdriver element: Email Instructions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_email_instructions
        )

    def get_full_name_editfield_label(self):
        """
        Get Full Name

        Returns:
              webdriver element: Full Name Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_full_name_label)

    def get_full_name_editfield(self):
        """
        Get Full Name

        Returns:
              webdriver element: Full Name Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_full_name_textfield)

    def get_full_name_instructions_textview(self):
        """
        Get Full Name Instructions

        Returns:
              webdriver element: Full Name Instructions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_full_name_instructions)

    def get_user_name_editfield_label(self):
        """
        Get User Name

        Returns:
              webdriver element: User Name Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_user_name_label)

    def get_user_name_editfield(self):
        """
        Get User Name

        Returns:
              webdriver element: User Name Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_user_name_textfield)

    def get_user_name_instructions_textview(self):
        """
        Get User Name Instructions

        Returns:
              webdriver element: User Name Instructions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_user_name_instructions)

    def get_password_editfield_label(self):
        """
        Get Password

        Returns:
              webdriver element: Password Element
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_password_label)

    def get_password_editfield(self):
        """
        Get Password

        Returns:
              webdriver element: Password Element
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_password_textfield)

    def get_password_instructions_textview(self):
        """
        Get Password Instructions

        Returns:
              webdriver element: Password Instructions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_password_instructions)

    def get_country_spinner_label(self):
        """
        Get Country Spinner

        Returns:
              webdriver element: Country Spinner Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_country_label)

    def get_country_spinner(self):
        """
        Get Country Spinner

        Returns:
              webdriver element: Country Spinner Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_country_dropdown)

    def get_country_spinner_instructions_textview(self):
        """
        Get Country Spinner Instructions

        Returns:
              webdriver element: Country Spinner Instructions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_country_instructions
        )

    def get_show_optional_fields_textview(self):
        """
        Get Show Option Fields

        Returns:
              webdriver element: Show Option Fields Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_show_optional_fields_textview
        )

    def get_create_my_account_textview(self):
        """
        Get Create My Account Textview

        Returns:
              webdriver element: Create My Account Element
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_instructions_textview())

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_create_my_account_button
        )

    def get_agreement_textview(self):
        """
        Get Terms Textview

        Returns:
              Webdriver element: Agree Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_agreement_textview
        )

    def show_optional_fields(self):
        """
        Show Option Fields

        Returns:
              webdriver element: Hide Optional Fields Element
        """

        self.get_show_optional_fields_textview().click()

        self.global_contents.scroll_from_element(self.driver, self.get_hide_optional_fields_textview())

        return self.get_hide_optional_fields_textview()

    def get_hide_optional_fields_textview(self):
        """
        Get Hide Option Fields

        Returns:
              webdriver element: hide Option Fields Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_hide_optional_fields_textview
        )

    def hide_optional_fields(self):
        """
        Hide Option Fields

        Returns:
              webdriver element: Show Optional Fields Element
        """

        self.get_hide_optional_fields_textview().click()

        return self.get_show_optional_fields_textview()

    def get_gender_textview(self):
        """
        Get Gender Label

        Returns:
              webdriver element: Gender Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_gender_label
        )

    def get_gender_spinner(self):
        """
        Get Gender Spinner

        Returns:
              webdriver element: Gender Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.register_all_dropdowns)[self.global_contents.second_existence]

    def load_gender_spinner(self):
        """
        Load Gender Spinner

        Returns:
              webdriver element: Gender dropdown Element
        """
        self.get_gender_spinner().click()

        self.get_gender_textview().click()

    def get_year_of_birth_textview(self):
        """
        Get Year of Birth label

        Returns:
              webdriver element: Year of Birth Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_year_of_birth_label
        )

    def get_year_of_birth_spinner(self):
        """
        Get Year of Birth spinner

        Returns:
              webdriver element: Year of Birth Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.register_all_dropdowns)[self.global_contents.third_existence]

    def load_year_of_birth_spinner(self):
        """
        Load year of birth dropdown

        Returns:
              webdriver element: Gender Element
        """
        self.get_year_of_birth_spinner().click()

        self.get_year_of_birth_textview().click()

    def get_education_textview(self):
        """
        Get Education label

        Returns:
              webdriver element: Education Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_education_label
        )

    def get_education_spinner(self):
        """
        Get Education Spinner

        Returns:
              webdriver element: Education Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            ios_elements.register_all_dropdowns)[self.global_contents.fourth_existence]

    def load_education_spinner(self):
        """
        Load Education Spinner

        Returns:
              webdriver element: Gender Element
        """
        self.get_education_spinner().click()

        self.get_education_textview().click()

    def get_goal_textview(self):
        """
        Get Goal label

        Returns:
              webdriver element: Goal Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_goal_label
        )

    def get_goal_textarea(self):
        """
        Get Goal TextArea

        Returns:
              webdriver element: Goal Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_goal_textarea
        )

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on Register screen
        """

        ios_new_landing_page = IosNewLanding(self.driver, self.log)

        if self.get_register_divider_textview().text == strings.REGISTER_SCREEN_REGISTER_WITH:
            self.driver.back()
            if ios_new_landing_page.load_register_screen().text == strings.REGISTER_SCREEN_REGISTER_WITH:
                self.log.info('Register screen is successfully loaded')
            else:
                self.log.error('New Landing screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.error('Not on Register screen')
            self.global_contents.flag = False

        return self.global_contents.flag

    def get_eula_textview(self):
        """
        Get EULA

        Returns:
             webdriver element: EULA Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_eula_textview
        )

    def get_terms_textview(self):
        """
        Get Terms

        Returns:
             webdriver element: Terms Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_terms_textview
        )

    def get_privacy_textview(self):
        """
        Get Privacy

        Returns:
             webdriver element: Privacy Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_privacy_textview
        )

    def get_agreement_close_button(self):
        """
        Get Close

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_terms_button
        )

    def load_eula_screen(self):
        """
        Load EULA screen and then close it

        Returns:
             webdriver element: Login Button Element
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_instructions_textview())
        self.get_eula_textview().click()
        self.get_agreement_close_button().click()

        return self.get_register_divider_textview()

    def load_terms_screen(self):
        """
        Load Terms screen and then close it

        Returns:
             webdriver element: Login Button Element
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_instructions_textview())
        self.get_terms_textview().click()
        self.get_agreement_close_button().click()

        return self.get_register_divider_textview()

    def load_privacy_screen(self):
        """
        Load Privacy screen and then close it

        Returns:
             webdriver element: Login Button Element
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_instructions_textview())
        self.get_privacy_textview().click()
        self.get_agreement_close_button().click()

        return self.get_register_divider_textview()

    def validate_required_optional_fields(self):
        """
        validate Email, Full Name, Username, Password & Country required fields

        Returns:
             bool: Returns True if validation error is visible when user try to register with blank fields
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_editfield())
        self.get_create_my_account_textview().click()

        output = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_error_alert_title_textview
        )

        if output:
            self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.register_error_alert_title_textview
            )
            self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.register_error_alert_textview
            )
            wrong_credentials_alert_ok = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.register_error_alert_button
            )
            wrong_credentials_alert_ok.click()

            return True

        else:
            return False

    def get_email_validation_textview(self):
        """
        Get Email validation error Textview

        Returns:
              Webdriver element: Email validation error Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_email_error
        )

    def get_full_name_validation_textview(self):
        """
        Get Full Name validation error Textview

        Returns:
              Webdriver element: Full Name validation error Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_full_name_error
        )

    def get_username_validation_textview(self):
        """
        Get Username validation error Textview

        Returns:
              Webdriver element: Username validation error Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_user_name_error
        )

    def get_password_validation_textview(self):
        """
        Get Password validation Textview

        Returns:
              Webdriver element: Password validation error Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_password_error
        )

    def get_country_validation_textview(self):
        """
        Get Country validation Textview

        Returns:
              Webdriver element: Country validation error Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_country_error
        )

    def submit_register_form(self, email, name, username, password, country):
        """
        Fill Register form

        Arguments:
            email (str): Email value
            name (str): Full Name
            username (str): User Name
            assword (str): Password
            country (str): Country
        """

        self.get_email_editfield().send_keys(email)
        self.get_full_name_editfield().send_keys(name)
        self.get_user_name_editfield().send_keys(username)
        self.global_contents.scroll_from_element(self.driver, self.get_user_name_editfield_label())
        self.get_password_editfield().send_keys(password)
        self.select_country(country)
        self.get_create_my_account_textview().click()

    def select_country(self, country):
        """
        Select Country value from spinner

        Arguments:
            country (str): Country
        """

        self.get_country_spinner().click()

        countries_list = self.global_contents.get_all_views_on_ios_screen(self.driver, ios_elements.all_pickwheels)[0]
        countries_list.send_keys(country)
