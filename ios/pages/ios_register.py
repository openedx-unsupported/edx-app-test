"""
    Register Page Module
"""
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


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
